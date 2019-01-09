# ms-cosmetics-analysis

Code for webscraping ranking data and cosmetic names / files from MMORPG MapleStory/MapleLegends.

Chickenscratch.py is in some sense the master file. The other files are pretty snippets from chickenscratch. This file is a little difficult to read since it is unedited to preserve the learning and debugging process for when using external libraries. Best to use an editor that can execute selected lines of code for this file.

One big warning is when taking the raw hairstyle images (which contain several replicates of different colours) and re-saving 1 grayscale copy. The code depends on the coordinates where your image editor opens, and also the amount of time for the computer to finishing executing the command+S and command+O prompts. The code will certainly fail if either of these are not tailored to your set-up. 

The final data collected in early November 2018 should look something like this: https://public.tableau.com/profile/kithara.koro#!/vizhome/ms-cosmetics-analysis_0/Dashboard1