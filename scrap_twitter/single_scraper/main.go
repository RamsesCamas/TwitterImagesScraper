package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	twitterscraper "github.com/n0madic/twitter-scraper"
)

func downloadFile(URL, fileName, folder string) error {
	//Get the response bytes from the url
	response, err := http.Get(URL)
	if err != nil {
		return err
	}
	defer response.Body.Close()

	if response.StatusCode != 200 {
		return errors.New("Received non 200 response code")
	}
	//Create a empty file
	path := fmt.Sprintf("%s/%s", folder, fileName)
	file, err := os.Create(path)
	if err != nil {
		return err
	}
	defer file.Close()

	//Write the bytes to the fiel
	_, err = io.Copy(file, response.Body)
	if err != nil {
		return err
	}

	return nil
}

func getImages(scraper twitterscraper.Scraper, tweetID string) []string {
	url_imgs := []string{}
	tweet, err := scraper.GetTweet(tweetID)
	if err != nil {
		panic(err)
	}
	imgs := tweet.Photos
	for _, img := range imgs {
		url_imgs = append(url_imgs, img)
	}
	return url_imgs
}

func readFile() []string {
	tweetsID := []string{}
	file, err := os.Open("../twint_py/no_importancia/NIM_tweetsIDs.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		tweetsID = append(tweetsID, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return tweetsID
}

func main() {
	scraper := twitterscraper.New()
	tweetsID := readFile()
	f, err := os.OpenFile("../twint_py/no_importancia/imgs_NIM.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	for _, tweetID := range tweetsID {
		url_imgs := getImages(*scraper, tweetID)
		for _, img := range url_imgs {
			if _, err = f.WriteString(img + "\n"); err != nil {
				panic(err)
			}
		}
	}
}
