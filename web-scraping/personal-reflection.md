# My personal experience using AI to "automate the boring stuff"

I was teaching myself Chinese and found a good website called https://www.strokeorder.com that had a large collection of Chinese handwriting worksheets. The problem is, it took quite some time to search the website, find the right one, scroll down the page, and download it. However, after inspecting the URLs for a few different ones, I found that the URLs all followed a standard format based on the Unicode for Chinese characters, and the download links were all accessible and well-formatted from the page HTML when I clicked "View Source" on it. The problem was, I had not gotten to the web scraping portion of the "Automate the Boring Stuff" book yet and so had no idea how to write a Python script to take in a list of characters and access the URLs.

So I asked o3 to write me a script for this, explaining the formatting used etc. in this prompt:

Write me some Python code that:

1. Takes a list of Chinese characters
2. For each one, goes to https://www.strokeorder.com/chinese/[insert character here]
3. Finds all links to PDFs on that page
4. Goes to those links
5. Downloads the PDFs

This worked fairly well, but did not download all the PDF links; because of the naming scheme it used, it inadvertently only downloaded the first link on each page, which was either portrait or landscape, seemingly at random. When I found out that it was doing that, I checked the URL formatting for all the links, realized I only wanted portrait worksheets, and gave this prompt:

OK, so one fix I want. Each one has two; a portrait one of the form https://www.strokeorder.com/assets/bishun/worksheets/pdf/1/25105.pdf and a landscape one of the form https://www.strokeorder.com/assets/bishun/worksheets/pdf/2/25105.pdf. I want only the portrait ones.

It then gave me a good script which I was able to make use of effectively to download the stroke order worksheets very quickly from a list of characters.

## "Knowing is half the battle"

Though I did read through the code and asked some questions about what exactly specific lines meant, that was not required to get it working, and the whole process required no actual coding on my part. However, it did require me to notice the consistency in the URL formatting, find a few shortcuts on my own (e.g. directly typing the URL as formatted instead of searching), and noticing the portrait vs. landscape inconsistency and the cause (which was an issue with giving files duplicate procedurally-generated names and then not saving duplicates). These are all skills that required some of my own coding knowledge, as much as this did seem to give me a slight speed-up over coding this from scratch or even copying a similar script from a book like "Automate the Boring Stuff" and adapting it as needed.

One key challenge the Stone Center would face would be in assessing how much of this sort of knowledge workers would have or not have, and how to teach this sort of knowledge to workers who could benefit from using AI-generated coding tools without having formal CS experience in advance.