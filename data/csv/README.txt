Thank you for downloading the TVSeries dataset! If you use this dataset, please refer to our arXiv paper: 
De Geest, R., Gavves, E., Ghodrati, A., Li, Z., Snoek, C. & Tuytelaars, T. (2016). Online Action Detection. arXiv preprint arXiv:1604.06506

The TVSeries dataset can be used for action recognition and detection. It consists of the first few episodes 
of six recent TV series: Breaking Bad, How I Met Your Mother, Mad Men, Modern Family, Sons of Anarchy, and 
24. Since we do not own the rights to these series, we cannot provide the videos to you. If you buy and 
rip the DVDs, you should be able to use our annotations. If you encounter any problem with the annotations 
or the videos, do not hesitate to send an e-mail to roeland.degeest@esat.kuleuven.be.

The annotations are provided 'as is'. We make no warranties regarding the TVSeries Dataset, including (but not
limited to) being up-to-date, correct or complete.
That said, we did our best to annotate everything correctly and accurately. If you still find errors, please 
send us an e-mail.

The file classes.txt contains a list of the 30 action classes annotated and the number of instances of these 
actions in the whole dataset.

There are three files with annotations (GT-train.txt, GT-val.txt and GT-test.txt), corresponding to the 
training, validation and testing set. Every line of a file contains one action instance. The annotation 
of an action instance consists of the following parts, separated by tabs:
	- series name and episode number (Name_Of_The_Series_epNUMBER)
	- class name (same as in classes.txt)
	- start of the action (in seconds)
	- end of the action (in seconds)
	- only one person visible? (yes/no (1/0))
	- atypical action instance (the person does something that is unusual for this action)? (yes/no)
	- shotcut during action? (yes/no)
	- moving camera during action? (yes/no)
	- person is very small or in background? (yes/no)
	- action is recorded from the front? (yes/no)
	- action is recorded from the side? (yes/no)
	- action is recorded from an unusual viewpoint? (yes/no)
	- action is (partly) spatially occluded (by object/person/...)? (yes/no)
	- action is spatially truncated (by frame border)? (yes/no)
	- beginning of the action is missing? (yes/no)
	- end of the action is missing? (yes/no)
	- comments concerning the content of the action or the degree of occlusion and truncation (optional)

