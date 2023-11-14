# yummarizer

This is a cli tool that can be used to summarize long youtube cooking videos into easy to understand recipes, instructions, and ingredients using generative AI.
I intend to make 

I cook a lot and the main source of my recipes come from youtube cooking videos. Often times when I find a recipe I liked I would have to 
either hope that there was a link to the written instructions in the video description, or I would have to have the video open and scrub through
while I was cooking(which blows) and occasionally leads to catastrophe. 
<p align="left">
  <img width="500"  src="https://media.tenor.com/XpQuXaxXE7AAAAAd/kitchen-burn.gif  alt="demo"/>
</p>

I made  yummarizer to streamline that whole experience so that I could just enjoy putting a meal together.
For now it is a cli tool that downloads a pdf of the summarization, but I plan to turn it into a web server and create a chrome plugin so 
that it can be used outside of a cli.

# Installation

- Download this repository
```bash
git clone https://github.com/yosief14/yummarizer.git
```
- Navigate to the project directory

```bash
cd yummarizer
```

- Install
```
pip install -e path/to/yummarizer
```

# Instructions
- This project uses OPENAI api for now and in order to work properly user will need to upload their own api key into
the .env file

- If you don't already have an api key the process to getting one is easy and instructions can be found [here](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

Once you have the .env setup usage of the tool looks like this
```
yummarize [youtuve_video_url] [path/to/save/pdf]
```

After, you will be prompted with an estimation of how much the process could cost before you send it 
```
The cost of this recipe is between 0.034329 and 0.018227999999999998 cents. Do you want to continue? (y/n)
```

If you don't specify a path it will default to your home directory

This tool only works with youtube videos that are capable of showing captions since I'm using auto generated transcriptions
to summarize the video.

# Disclaimer
At the end of the Day this tool relies on a generative AI which could lead to inaccurate summarizations ranging from excluding measurements for an ingredient
to completely hallucinate an entire recipe. While I may have not run into any considerable issues with accuracy It is still very much possible you do so take
this program's output with a grain of salt. 

# TODO
🔲 I want to use other LLMs  that can run locally like LLama or GPT4all so user will not have to use their own api key

🔲 Upload file to web server

🔲 Create chrome plugin that points to the server

🔲 Implement Google Drive functionality so recipes can be saved to users cloud drive



