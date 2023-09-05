# HighlightAndroidGui
<p> A program which highlights leaf-level GUI components in pngs of Android application screenshots. 
The xml files are captured by using the dump feature of the UI Automator framework in Android.</p>
<H2> Set up</H1></p>
<ol>
<li>Install requirements through command line </li>

```
pip install -r requirements.txt
```
<li> Ensure png and xml file pairs have the same name</li>
<li> GO TIME!</li>
</ol>
<H2>Running the program</H2>
<p>To run the code, you will input the python command with the py file along with the filepath of the file you wish to run the code on. 
  Because the png and xml file's have the same name, type that filepath without the extension </p>
  <p> Ex) If the png and xml files are "com.apalon.ringtones.png" and "com.apalon.ringtones.xml": </p>

```
python leafHighlighter.py com.apalon.ringtones
```
<p> You may enter multiple files:</p>

```
python leafHighlighter.py com.giphy.messenger-1 com.giphy.messenger-2
```
  
