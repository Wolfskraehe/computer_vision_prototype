Readme Video Tracker

The environment.yaml file list all necessary dependencies for the tracker.
If you are using miniconda or anaconda you can use: conda env -f environment.yml to create an environment with all necessary
libraries, or you can use the environment.yml file for a pakage system of your choice.

The files final.ipynb, utils.py and tracker.py contain the code and must be in the same folder to work.
If you provide a folder "videos" with video files, in the same folder as the code files, you simply can run all cells of the final.ipynb file
and the tracker will create an "output" folder in the root directory of the code, where the results of the provided videos will be stored.
The tracker shows a progress bar while processing the videos.

If you want to change the path to your input or output videos you can do this in the first block of final.ipynb in these lines:
	video_path = "videos" 
	output_path = "outputs"
	
	
Please provide an absolut path.

The tracker needed around 9 minutes for all provided 28 videos on an outdated pc system, but performance can vary depending on system and videos. 
