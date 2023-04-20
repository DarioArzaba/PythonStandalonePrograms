import PySimpleGUI as sg
import pandas as pd
import math

dataTable = {'CatalogNumber': ['KHG1-20', 'KHG1-22', 'KHG1-24', 'KHG1-25', 'KHG1-28', 
							   'KHG1-30', 'KHG1-32', 'KHG1-35', 'KHG1-36', 'KHG1-40',
							   'KHG1-44', 'KHG1-45', 'KHG1-48', 'KHG1-50', 'KHG1-60', 
							   'KHG1-70', 'KHG1-80', 'KHG1-90', 'KHG1-100',
							   'KHG1.5-20', 'KHG1.5-22', 'KHG1.5-24', 'KHG1.5-25', 'KHG1.5-26', 
							   'KHG1.5-28', 'KHG1.5-30', 'KHG1.5-32', 'KHG1.5-35', 'KHG1.5-36',
							   'KHG1.5-40', 'KHG1.5-44', 'KHG1.5-45', 'KHG1.5-48', 'KHG1.5-50', 
							   'KHG1.5-52', 'KHG1.5-60', 'KHG1.5-70', 'KHG1.5-80', 'KHG1.5-90', 'KHG1.5-100',
							   'KHG2-15', 'KHG2-16', 'KHG2-18', 'KHG2-20', 'KHG2-22', 
							   'KHG2-24', 'KHG2-25', 'KHG2-26', 'KHG2-28', 'KHG2-30',
							   'KHG2-32', 'KHG2-35', 'KHG2-36', 'KHG2-40', 'KHG2-44', 
							   'KHG2-45', 'KHG2-48', 'KHG2-50', 'KHG2-52', 'KHG2-60',
							   'KHG2-70', 'KHG2-80', 'KHG2-90', 'KHG2-100',
							   'KHG2.5-15', 'KHG2.5-16', 'KHG2.5-18', 'KHG2.5-20', 'KHG2.5-22', 
							   'KHG2.5-24', 'KHG2.5-25', 'KHG2.5-26', 'KHG2.5-28', 'KHG2.5-30',
							   'KHG2.5-32', 'KHG2.5-35', 'KHG2.5-36', 'KHG2.5-40', 'KHG2.5-44', 
							   'KHG2.5-45', 'KHG2.5-48', 'KHG2.5-50', 'KHG2.5-52', 'KHG2.5-60',
							   'KHG3-15', 'KHG3-16', 'KHG3-18', 'KHG3-20', 'KHG3-22', 
							   'KHG3-24', 'KHG3-25', 'KHG3-26', 'KHG3-28', 'KHG3-30',
							   'KHG3-32', 'KHG3-35', 'KHG3-36', 'KHG3-40', 'KHG3-44', 
							   'KHG3-45', 'KHG3-48', 'KHG3-50', 'KHG3-52', 'KHG3-60'
							   ],
			 'Module':  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
						 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
						 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
						 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5,
						 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
			 'ToothWidth':  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
						 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
						 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
						 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
						 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
			 'NumberTeeth':  [20, 22, 24, 25, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 60, 70, 80, 90, 100,
							  20, 22, 24, 25, 26, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 52, 60, 70, 80, 90, 100,
							  15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 52, 60, 70, 80, 90, 100,
							  15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 52, 60,
							  15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 52, 60],
			 'BoreA':        [6, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12, 12, 15, 15, 15,
							  12, 12, 12, 12, 12, 15, 15, 15, 15, 15, 15, 15, 18, 18, 18, 18, 20, 20, 20, 20, 20,
							  12, 12, 12, 15, 15, 15, 15, 15, 15, 18, 18, 18, 18, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25,
							  15, 15, 15, 18, 18, 18, 20, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25,
							  18, 18, 18, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25, 25, 30, 30, 30],
			 'HubDiameterB':      [17, 18, 20, 20, 20, 25, 25, 25, 25, 30, 30, 30, 30, 35, 40, 40, 50, 50, 50,
								   24, 26, 28, 30, 32, 36, 38, 40, 42, 45, 50, 50, 50, 50, 60, 60, 60, 60, 70, 70, 70,
								   24, 26, 30, 32, 36, 38, 40, 42, 45, 50, 50, 50, 50, 60, 60, 60, 60, 60, 65, 65, 70, 80, 90, 100,
								   30, 32, 38, 40, 44, 48, 50, 50, 60, 65, 70, 70, 70, 70, 75, 75, 75, 80, 80, 80,
								   36, 38, 40, 50, 54, 58, 60, 60, 70, 75, 75, 80, 80, 80, 80, 80, 85, 85, 85, 90],
			 'PitchDiameterC':    [20, 22, 24, 25, 28, 30, 32, 35, 36, 40, 44, 45, 48, 50, 60, 70, 80, 90, 100,
								   30, 33, 36, 37.5, 39, 42, 45, 48, 52.5, 54, 60, 66, 67.5, 72, 75, 78, 90, 105, 120, 135, 150,
								   30, 32, 36, 40, 44, 48, 50, 52, 56, 60, 64, 70, 72, 80, 88, 90, 96, 100, 104, 120, 140, 160, 180, 200,
								   37.5, 40, 45, 50, 55, 60, 62.5, 65, 70, 75, 80, 87.5, 90, 100, 110, 112.5, 120, 125, 130, 150,
								   45, 48, 54, 60, 66, 72, 75, 78, 84, 90, 96, 105, 108, 120, 132, 135, 144, 150, 156, 180],
			 'ExternalDiameterD': [22, 24, 26, 27, 30, 32, 34, 37, 38, 42, 46, 47, 50, 52, 62, 72, 82, 92, 102,
								   33, 36, 39, 40.5, 42, 45, 48, 51, 55.5, 57, 63, 69, 70.5, 75, 78, 81, 93, 108, 123, 138, 153,
								   34, 36, 40, 44, 48, 52, 54, 56, 60, 64, 68, 74, 76, 84, 92, 94, 100, 104, 108, 124, 144, 164, 184, 204,
								   42.5, 45, 50, 55, 60, 65, 67.5, 70, 75, 80, 85, 92.5, 95, 105, 115, 117.5, 125, 130, 135, 155,
								   51, 54, 60, 66, 72, 78, 81, 84, 90, 96, 102, 111, 114, 126, 138, 141, 150, 156, 162, 186],
			 'AllowableTorqueBending': [7.79, 8.92, 10.1, 10.7, 12.4, 13.6, 13.5, 15.1, 15.7, 17.9, 20.2, 20.7, 22.5, 23.6, 29.3, 35.2, 41.0, 46.9, 50.4,
										26.3, 27.4, 30.9, 32.7, 34.5, 38.1, 41.8, 45.5, 51.1, 52.9, 60.5, 68.1, 70.0, 75.8, 79.6, 83.5, 99.1, 114, 132, 151, 170,
										40.5, 40.6, 48.5, 56.6, 64.9, 73.3, 77.5, 81.8, 90.4, 99.1, 108, 121, 126, 143, 161, 166, 172, 181, 189, 225, 269, 301, 344, 387,
										71.8, 79.4, 94.8, 111, 127, 143, 151, 160, 176, 193, 211, 236, 245, 268, 302, 310, 336, 353, 370, 439,
										129, 143, 171, 199, 228, 258, 272, 287, 318, 348, 363, 407, 422, 482, 543, 558, 604, 635, 666, 757],
			 'AllowableTorqueSurface': [4.98, 6.14, 7.43, 8.12, 10.4, 12.1, 12.6, 15.4, 16.3, 20.5, 25.3, 26.5, 30.5, 33.3, 49.4, 68.9, 91.8, 118, 142, 
										18.5, 20.8, 25.3, 27.7, 30.2, 35.7, 41.6, 48.0, 58.5, 62.2, 78.5, 96.8, 102, 117, 128, 140, 191, 256, 343, 442, 554,
										22.8, 24.1, 31.9, 40.8, 50.6, 61.4, 67.3, 73.4, 86.6, 101, 117, 142, 151, 191, 236, 248, 273, 299, 326, 447, 625, 799, 1030, 1290,
										41.1, 47.9, 63.4, 81.3, 101, 122, 134, 146, 173, 201, 232, 284, 302, 265, 451, 474, 547, 599, 652, 890,
										74.7, 87.2, 115, 148, 184, 224, 245, 268, 316, 369, 407, 498, 530, 670, 828, 869, 1000, 1090, 1190, 1560],
			 'Backlash': [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.14, 0.14, 0.14, 0.14, 0.14,
						  0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.16, 0.16, 0.16, 0.16,
						  0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19,
						  0.15, 0.15, 0.15, 0.15, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19,
						  0.15, 0.15, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19, 0.19],
			 'Weight': [0.034, 0.037, 0.046, 0.048, 0.056, 0.072, 0.078, 0.088, 0.091, 0.12, 0.14, 0.14, 0.16, 0.18, 0.26, 0.32, 0.44, 0.53, 0.62,
						0.088, 0.11, 0.13, 0.15, 0.17, 0.19, 0.22, 0.26, 0.30, 0.33, 0.42, 0.47, 0.47, 0.52, 0.63, 0.67, 0.81, 1.02, 1.37, 1.65, 1.97,
						0.11, 0.13, 0.17, 0.20, 0.25, 0.30, 0.33, 0.37, 0.43, 0.50, 0.55, 0.63, 0.65, 0.85, 0.98, 1.02, 1.13, 1.16, 1.29, 1.65, 2.21, 2.93, 3.73, 4.64,
						0.20, 0.24, 0.33, 0.38, 0.47, 0.57, 0.61, 0.65, 0.83, 0.97, 1.13, 1.28, 1.34, 1.53, 1.85, 1.92, 2.13, 2.35, 2.51, 3.20,
						0.36, 0.42, 0.53, 0.70, 0.86, 1.03, 1.12, 1.19, 1.47, 1.65, 1.82, 2.17, 2.27, 2.69, 3.16, 3.28, 3.75, 3.95, 4.24, 5.57]}

df = pd.DataFrame(data=dataTable)

def createDFAll(dataFrame, gearRatio):

	firstGear = []
	firstGearModule = []
	firstGearNumberTeeth = []
	secondGear = []
	secondGearModule = []
	secondGearNumberTeeth = []
	firstStageName = []
	firstStageRatio = []
	thirdGear = []
	thirdGearModule = []
	thirdGearNumberTeeth = []
	fourthGear = []
	fourthGearModule = []
	fourthGearNumberTeeth = []
	secondStageName = []
	secondStageRatio = []

	gearFirstSize = []
	gearSecondSize = []
	gearFirstSizeMax = []
	gearSecondSizeMax = []
	gearSizeMaxR = []

	gearNamesR = []
	gearRatioR = []

	for row in dataFrame.index:
		firstGear.append(dataFrame['CatalogNumber'][row])
		firstGearModule.append(dataFrame['Module'][row])
		firstGearNumberTeeth.append(dataFrame['NumberTeeth'][row])
		secondGear.append(dataFrame['CatalogNumber'][row])
		secondGearModule.append(df['Module'][row])
		secondGearNumberTeeth.append(dataFrame['NumberTeeth'][row])
		thirdGear.append(dataFrame['CatalogNumber'][row])
		thirdGearModule.append(dataFrame['Module'][row])
		thirdGearNumberTeeth.append(dataFrame['NumberTeeth'][row])
		fourthGear.append(dataFrame['CatalogNumber'][row])
		fourthGearModule.append(dataFrame['Module'][row])
		fourthGearNumberTeeth.append(dataFrame['NumberTeeth'][row])
		gearFirstSize.append(dataFrame['ExternalDiameterD'][row])
		gearSecondSize.append(dataFrame['ExternalDiameterD'][row])
		

	for i in range(len(firstGearNumberTeeth)):
		for j in range(len(secondGearNumberTeeth)):
			if firstGearModule[i] == secondGearModule[j]:
				firstStageName.append(firstGear[i] + " " + secondGear[j])
				firstStageRatio.append(firstGearNumberTeeth[i]/secondGearNumberTeeth[j])
				gearFirstSizeMax.append(gearFirstSize[i] + gearSecondSize[j])

	for i in range(len(thirdGearNumberTeeth)):
		for j in range(len(fourthGearNumberTeeth)):
			if thirdGearModule[i] == fourthGearModule[j]:
				secondStageName.append(thirdGear[i] + " " + fourthGear[j])
				secondStageRatio.append(thirdGearNumberTeeth[i]/fourthGearNumberTeeth[j])
				gearSecondSizeMax.append(gearFirstSize[i] + gearSecondSize[j])

	for i in range(len(firstStageRatio)):
		for j in range(len(secondStageRatio)):
			gearNamesR.append(firstStageName[i] + " + " + secondStageName[j])
			gearRatioR.append(firstStageRatio[i] * secondStageRatio[j])
			gearSizeMaxR.append(max([gearFirstSizeMax[i], gearSecondSizeMax[j]]))

	dfT = pd.DataFrame(list(zip(firstStageName, firstStageRatio, secondStageName, secondStageRatio)), columns =['FirstStage', 'FirstRatio', 'SecondStage', 'SecondRatio'])
	dfR = pd.DataFrame(list(zip(gearNamesR, gearRatioR, gearSizeMaxR)), columns =['GearNamesR', 'GearRatioR', 'GearSizeMax'])
	df_sort1 = dfR.iloc[(dfR['GearRatioR']-gearRatio).abs().argsort()[:100]]
	df_sort2 = df_sort1.sort_values("GearSizeMax")
	df_sort3 = df_sort2.head(30)
	return df_sort3

sg.theme('Default')
# print(sg.ListOfLookAndFeelValues())

layout_t = [[sg.Text('DESCRIPTION')],
			[sg.Text('Gearbox Size Length (in)')],
			[sg.Text('Gearbox Size Width (in)')],
			[sg.Text('Gearbox Size Height (in)')],
		  	[sg.Text('Steady State Input Speed (rpm)')],
		 	[sg.Text('Steady State Output Speed Min (rpm)')],
		  	[sg.Text('Steady State Output Speed Max (rpm)')],
		  ]

layout_r = [[sg.Text('VALUE')],
			[sg.Input(key='-GearboxSizeLength-', default_text='14')],
			[sg.Input(key='-GearboxSizeWidth-', default_text='14')],
			[sg.Input(key='-GearboxSizeHeight-', default_text='22')],
			[sg.Input(key='-SteadyStateInputSpeed-', default_text='1750')],
		  	[sg.Input(key='-SteadyStateOutputSpeedMin-', default_text='82')],
		  	[sg.Input(key='-SteadyStateOutputSpeedMax-', default_text='88')],
			]

layout_o = [[sg.Multiline(key='-MULTILINEKEY-', size=(100,30))]]

layout = [
		[sg.Col(layout_t, p=0), sg.Col(layout_r, p=0), sg.Col(layout_o, p=0)],
		[sg.HorizontalSeparator()],
		[sg.Button('Calculate'), sg.Button('Exit')]]

window = sg.Window('Gear Combinations', layout)



while True:
	event, values = window.read()
	#print(event, values)
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	if event == 'Calculate':
		gearRatioValue = float(values['-SteadyStateInputSpeed-'])/((float(values['-SteadyStateOutputSpeedMin-']) + float(values['-SteadyStateOutputSpeedMax-']))/2)
		dfClosest = createDFAll(df, gearRatioValue)
		window['-MULTILINEKEY-'].print(dfClosest)

window.close()