# Bilibili & Youtube Comment Analysis


<b>Project Intention</b>: Fetching the Comments from Bilibili and Youtube to extract key insights and perform sentiment analysis.<br>

<b>Short description</b>:<br> 
The folder include two python file. Each of them is a specification to fetching and analyis a certain website's comment. Within each file, there are <b>4 First Level section</b> starting with #:<ol>
<li>XX Customization (Only change according to note ##)</li>
<li>Helper Function</li>
<li>Customization Parameter (Where you can customize)</li>
<li>Main Function</li>
</ol> 

After running the program, Excels (and sentiment analysis graph for bilibili) for each video you set in Customization Parameter section would be generated. Within the excel, Sheet1 contains all the comments. Sheet "Fomula" contains the ready to use fomula, but required plugin is needed.

<br>
<b>Required Tools</b>: Python, Excel Plug_in, OpenAI API

<b>Required Dependencies:</b><br>
<ol>Python: 3.8+ (Library Listed Below: Install using "pip install xxx" or "conda install -c conda-forge xxx")
</ol>
<ul>
    <ol>
    <li>requests (Suggested Version: 2.29)</li>
    <li>numpy</li>
    <li>pandas</li>
    <li>openpyxl</li>
    <li>matplotlib</li>
    <li>snownlp</li>
    <li>google-api-python-client</li>
    </ol>
</ul>
<br>

<ol>Excel (Suggested Version: Excel 2021) [Plugin List below]
</ol>
<ul>
    <ol>
    <li>ChatGPT for Excel (Developed by APPS do WONDERS) [chatgpt 3.5 is recommended]</li>
    </ol>
</ul>
<br>

<ol>OpenAI API 
</ol>
<ul>
    <ol>
    <li>Noted that both the Plugin and the API are paid services (How to set up payment can be found online)</li>
    </ol>
</ul>
<br>

<b>Installation Guide:</b>

<ol>Python: <ul><li>

https://www.python.org/downloads</li></ul> 
</ol> 
</ol>

<ol>Excel Plugin: (First 3 minutes) <ul>
<li>

https://www.youtube.com/watch?v=zi8DFS0iTTQ</li></ul> 
</ol>

<br>



<b>Future Plan:</b>
<ol>
<li>Implementing sentiment analysis for Youtube comments</li>
<li>Implementing analysis for transcript for Youtube video</li>
</ol>
<br>

<b>Acknowledgements:</b>
<ol>
<li> 

https://www.youtube.com/watch?v=zi8DFS0iTTQ
</li>
<li> 

https://www.youtube.com/watch?v=SIm2W9TtzR0 
</li>
<li>

https://www.bilibili.com/video/BV18C4y1H7mr
</li>

</ol>