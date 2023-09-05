# HighlightAndroidGui
<p> A program which highlights leaf-level GUI components in pngs of Android application screenshots. 
The xml files are captured by using the dump feature of the UI Automator framework in Android.</p>
<H2> Set up</H1></p>
<ol>
<li>Install requirements through command line </li>

```
pip install -r requirements.txt
```
<li> Ensure png and xml file pairs have the same name. Also ensure the files are in the same directory as leafHighlighter.py</li>
<li> GO TIME!</li>
</ol>
<H2>Running the program</H2>
<p>To run the code, you will input the python command with the py file along with the filename of the files you wish to run the code on. 
  Because the png and xml file's have the same name, type that filename without the extension </p>
  <p> Ex. If the png and xml files are "com.apalon.ringtones.png" and "com.apalon.ringtones.xml": </p>

```
python leafHighlighter.py com.apalon.ringtones
```
<p> You may enter multiple files:</p>

```
python leafHighlighter.py com.giphy.messenger-1 com.giphy.messenger-2
```

<h2>OUPUT</h2>
<p>The program will create an "output" directory with the results. ENJOY! </p>

<h3>My solution and decisions</h3>
<p>I decided to make the user only type in one filename of the pair without extensions to prevent extra work for them (considering they have the same name and are always xml and png). My solution takes that filename and adds the xml extension to access the xml file. It also adds the png extension to open the png file for drawing. It splits the xml file up up by nodes and determines leaf nodes by string search. Once found it searches for the bounds within that node using the re module (seemed to be the easiest approach). The Pillow library is used to draw on the original screenshot based on those bounds. It creates an output directory (if not already there) and saves the new image there for the user to view. Originally it just showed the images in a popup but that's bothersome for multiple files.<p>
