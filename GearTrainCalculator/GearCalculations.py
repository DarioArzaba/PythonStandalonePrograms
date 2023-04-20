from cmath import cos, sqrt
import PySimpleGUI as sg
import pandas as pd
import math

sg.theme('DefaultNoMoreNagging')

def SpeedReductionGear(teethNumFirst, teethNumSecond):
	return float(teethNumFirst)/float(teethNumSecond)

def SpeedReductionGears(teethNumFirst, teethNumSecond):
	return float(teethNumSecond)/float(teethNumFirst)

def NormalDiameterPitch(numberTeeths, diametralPitch):
	first = numberTeeths[0]/diametralPitch[0]
	second = numberTeeths[1]/diametralPitch[1]
	third = numberTeeths[2]/diametralPitch[2]
	fourth = numberTeeths[3]/diametralPitch[3]
	listGears = [first, second, third, fourth]
	averageListGears = sum(listGears) / len(listGears)
	return round(averageListGears)
	
def Velocity(d, n):
	return (math.pi * float(d) * float(n)) / 12

def Power(eff, obj, num):
	if num == 3:
		return (((abs(float(eff)-100)/100)+1)) * (num/3) * float(obj) 
	else:
		return (((((abs(float(eff)-100)/100)+1)) * float(obj))-float(obj)) * (num/3) + float(obj) 

def PowerDelivered(H, V):
	return (33000)*(float(H)/float(V))

def TransverCircularP(Pn, HelixAngle):
	return (float(Pn))*math.cos(math.radians(float(HelixAngle)))

def BValue(Qv):
	return 0.25*(12-float(Qv)) ** (2/3)

def AValue(B):
	return 50 + (56*(1-float(B)))

def VelocityFactor(A, B, V):
	return (((float(A) + sqrt(float(V)))/float(A))**float(B)).real

def GearBendingStress(W, K0, KV, KS, PT, F, KM, KB, J):
	return (float(W)*float(K0)*float(KV)*float(KS))*(float(PT)/float(F))*((float(KM)*float(KB))/float(J))

def BendingStrength(grade, hardness):
	if float(grade) == 1.0:
		return (77.3*float(hardness))+12800
	else:
		return (102*float(hardness))+16400

def StressCycleFactor(L, m, typeG):
	if float(typeG) == 1.0:
		return 1.6831*float(L)**(-0.0323)
	else:
		return 1.6831*(float(L)/float(m))**(-0.0323)

def BendingEndStrength(ST, SF, YN, KT, KR):
	return (float(ST)/float(SF))*((float(YN))/(float(KT)*float(KR)))

def SafetyFactor(Gall, G):
	return float(Gall)/float(G)

def SystemSafetyFactor(SFP, SFG):
	if float(SFP) < float(SFG):
		return "System Bending at Pinion with " + str(round(float(SFP), 3))
	elif float(SFP) > float(SFG):
		return "System Bending at Gear with " + str(round(float(SFG), 3))
	else:
		return "Equal system bending."

def TransversePressure(angleA, angleB):
	return math.degrees(math.atan( math.tan(math.radians(float(angleA))) / math.cos(math.radians(float(angleB))) ))

def NormalCircularPitch(Pn):
	return math.pi / float(Pn)

def NormalBasePitch(pn, angleA):
	return float(pn) * math.cos(math.radians(float(angleA)))

def PitchCircleRadius(dp, m, typeG):
	if float(typeG) == 1.0:
		return float(dp)/2
	else:
		return (float(m))* (float(dp)/2)

def ModifyingFactor(Pn):
	return 1/float(Pn)

def BaseCircleRadius(rp, angleC, m, typeG):
	result = float(rp) * math.cos(math.radians(float(angleC)))
	if float(typeG) == 1.0:
		return result
	else:
		return (float(m))* result

def AValueWear(a, rp, rbp):
	return ((((float(rp)+float(a))**2)-((float(rbp))**2))**(1/2)).real

def BValueWear(a, rg, rbg):
	return ((((float(rg)+float(a))**2)-((float(rbg))**2))**(1/2)).real

def CValueWear(rp, rg, angleC):
	return (float(rp) + float(rg)) * math.sin(math.radians(float(angleC)))

def TransverseLineZ(A, B, C):
	return float(A) + float(B) - float(C)

def LoadSharingRatio(pN, Z):
	return ((float(pN))/(float(Z)*0.95))

def GeometryFactorW(angleC, mN, m):
	return ((math.cos(math.radians(float(angleC))) * math.sin(math.radians(float(angleC))))/(2*float(mN))) * ((float(m))/(float(m) + 1)) 

def ContactStressW(Cp, Wt, K0, KV, KS, KM, dp, F, CF, I):
	return (float(Cp))*(sqrt(float(Wt)*float(K0)*float(KV)*float(KS)*((float(KM))/(float(dp)*float(F)))*((float(CF))/(float(I))) ).real)

def SurfaceEnduranceStrengthW(HB, typeGrade):
	if float(typeGrade) == 1.0:
		return (322*float(HB))+29100 
	else:
		return (349*float(HB))+34300

def StressCycleFactorWear(L, m ,tyoeG):
	if float(tyoeG) == 1.0:
		return 2.466*float(L)**(-0.056)
	else:
		return 2.466*(float(L)/float(m))**(-0.056)

def WearStress(SC, ZN, CH, SH, KT, KR):
	return ((float(SC)*float(ZN)*float(CH))/(float(SH)*float(KT)*float(KR)))

def SafetyFactorWear(GCall, GC):
	return float(GCall)/float(GC)

def SystemWear(SHP, SHG):
	if float(SHP) < float(SHG):
		return "System Wear at Pinion with " + str(round(float(SHP), 3))
	elif float(SHP) > float(SHG):
		return "System Wear at Gear with " + str(round(float(SHG), 3))
	else:
		return "Equal system wear."

def OverallSystemWear(SHP, SHG, SFP, SFG):
	bending = 0
	if float(SFP) < float(SFG):
		bending = float(SFP)
	elif float(SFP) > float(SFG):
		bending = float(SFG)
	wear = 0
	if float(SHP) < float(SHG):
		wear = float(SHP)
	elif float(SHP) > float(SHG):
		wear = float(SHG)
	wear2 = wear**2
	if bending < wear2 :
		return "Overall SF of Mesh " + str(round(float(bending), 3))
	elif bending > wear2 :
		return "Overall SF of Mesh " + str(round(float(wear2), 3))

#window[my_key].set_tooltip('New Tooltip')


layout_t = [[sg.Text('DESCRIPTION')],
			[sg.Text('First Gear Number Teeth (n2)')],
			[sg.Text('Second Gear Number Teeth (n3)')],
			[sg.Text('Third Gear Number Teeth (n4)')],
			[sg.Text('Fourth Gear Number Teeth (n5)')],
			[sg.Text('First Gear Diameter (in)')],
			[sg.Text('Second Gear Diameter (in)')],
			[sg.Text('Third Gear Diameter (in)')],
			[sg.Text('Fourth Gear Diameter (in)')],
			[sg.Text('First Gear Pitch D (in)')],
			[sg.Text('Second Gear Pitch D (in)')],
			[sg.Text('Third Gear Pitch D (in)')],
			[sg.Text('Fourth Gear Pitch D (in)')],
			[sg.Text('Face Width F (in)')],
			[sg.Text('Helix Angle (Ψ)')],
			[sg.Text('Pressure Angle (ϕ)')],
			[sg.Text('Steady State Input Speed (rpm)')],
			[sg.Text('Power Output (hp)')],
			[sg.Text('Efficiency (%)')],
			[sg.Text('Life Cycles')],
			[sg.Text('Quality Factor (QV)')],
			[sg.Text('Brinell Hardness (HB)')],
			[sg.Text('Geometry Factor N2N3 JP (Graph)')],
			[sg.Text('Geometry Factor N3N3 JG (Graph)')],
			[sg.Text('Geometry Factor N4N5 JP (Graph)')],
			[sg.Text('Geometry Factor N4N5 JG (Graph)')],
			[sg.Text('Steel Through Hardened Grade (1-2)')],
			[sg.Text('Overload Factor KO (Table)')],
			[sg.Text('Size Factor KS')],
			[sg.Text('Load Distribution Factor KM')],
			[sg.Text('Rim Thickness Factor KB')],
			[sg.Text('Bending Safety Factor SF')],
			[sg.Text('Wear Safety Factor SF')],
			[sg.Text('Temperature Factor KT')],
			[sg.Text('Reliability Factor KR (Table)')],
			[sg.Text('Surface Condition Factor CF')],
			[sg.Text('Hardness Ratio Factor CH')],
			[sg.Text('Elastic Coefficient CP (Table)')],
			[sg.Text('YAN2 - Distance Shaft to First Bearing N2')],
			[sg.Text('YBN2 - Distance Shaft to Second Bearing N2')],
			[sg.Text('YN2 - Distance Shaft to Gear N2')],
			[sg.Text('ZAN2 - Distance Shaft to First Bearing N2')],
			[sg.Text('ZBN2 - Distance Shaft to Second Bearing N2')],
			[sg.Text('ZN2 - Distance Shaft to Gear N2')],
			[sg.Text('YAN3N4 - Distance Shaft to First Bearing N3N4')],
			[sg.Text('YBN4N4 - Distance Shaft to Second Bearing N3N4')],
			[sg.Text('YN3 - Distance Shaft to Gear N3')],
			[sg.Text('YN4 - Distance Shaft to Gear N4')],
			[sg.Text('ZAN3N4 - Distance Shaft to First Bearing N3N4')],
			[sg.Text('ZBN3N4 - Distance Shaft to Second Bearing N3N4')],
			[sg.Text('ZN3 - Distance Shaft to Gear N3')],
			[sg.Text('ZN4 - Distance Shaft to Gear N4')],
			[sg.Text('YAN5 - Distance Shaft to First Bearing N5')],
			[sg.Text('YBN5 - Distance Shaft to Second Bearing N5')],
			[sg.Text('YN5 - Distance Shaft to Gear N5')],
			[sg.Text('ZAN5 - Distance Shaft to First Bearing N5')],
			[sg.Text('ZBN5 - Distance Shaft to Second Bearing N5')],
			[sg.Text('ZN5 - Distance Shaft to Gear N5')],

			[sg.HorizontalSeparator()],
			[sg.Button('Calculate')]
		  ]

layout_r = [[sg.Text('VALUE')],
			
			[sg.Input(key='-FirstGearNT-', default_text='20')],
			[sg.Input(key='-SecondGearNT-', default_text='90')],
			[sg.Input(key='-ThirdGearNT-', default_text='22')],
			[sg.Input(key='-FourthGearNT-', default_text='100')],
			[sg.Input(key='-FirstGearD-', default_text='1.360')],
			[sg.Input(key='-SecondGearD-', default_text='6.113')],
			[sg.Input(key='-ThirdGearD-', default_text='1.494')],
			[sg.Input(key='-FourthGearD-', default_text='6.792')],
			[sg.Input(key='-FirstGearPD-', default_text='1.18')],
			[sg.Input(key='-SecondGearPD-', default_text='5.315')],
			[sg.Input(key='-ThirdGearPD-', default_text='1.3')],
			[sg.Input(key='-FourthGearPD-', default_text='5.9')],
			[sg.Input(key='-FaceWidth-', default_text='5')],
			[sg.Input(key='-HelixAngle-', default_text='30')],
			[sg.Input(key='-PressureAngle-', default_text='20')],
			[sg.Input(key='-SteadyStateInput-', default_text='1750')],
			[sg.Input(key='-PowerOutput-', default_text='40')],
			[sg.Input(key='-Efficiency-', default_text='100')],
			[sg.Input(key='-LifeCycles-', default_text='10000000')],
			[sg.Input(key='-QualityFactor-', default_text='7')],
			[sg.Input(key='-HardnessBrinell-', default_text='552')],
			[sg.Input(key='-GeometryFactorJP-', default_text='0.4646')],
			[sg.Input(key='-GeometryFactorJG-', default_text='0.5198')],
			[sg.Input(key='-GeometryFactorJPN4N5-', default_text='0.4747')],
			[sg.Input(key='-GeometryFactorJGN4N5-', default_text='0.5198')],
			[sg.Input(key='-SteelHardGrade-', default_text='2')],
			[sg.Input(key='-OverloadFactor-', default_text='1.125')],
			[sg.Input(key='-SizeFactor-', default_text='1')],
			[sg.Input(key='-LoadDistributionFactor-', default_text='1')],
			[sg.Input(key='-RimThicknessFactor-', default_text='1')],
			[sg.Input(key='-SafetyFactor-', default_text='1')],
			[sg.Input(key='-SafetyFactorWear-', default_text='1')],
			[sg.Input(key='-TemperatureFactor-', default_text='1')],
			[sg.Input(key='-ReliabilityFactor-', default_text='0.85')],
			[sg.Input(key='-SurfaceConditionFactor-', default_text='1')],
			[sg.Input(key='-HardnessRatioFactorWear-', default_text='1')],
			[sg.Input(key='-ElasticCoefficient-', default_text='2300')],
			[sg.Input(key='-YAN2-', default_text='1')],
			[sg.Input(key='-YBN2-', default_text='6.4')],
			[sg.Input(key='-YN2-', default_text='3.2')],
			[sg.Input(key='-ZAN2-', default_text='1')],
			[sg.Input(key='-ZBN2-', default_text='6.4')],
			[sg.Input(key='-ZN2-', default_text='3.2')],
			[sg.Input(key='-YAN3N4-', default_text='1')],
			[sg.Input(key='-YBN4N4-', default_text='13')],
			[sg.Input(key='-YN3-', default_text='4.2')],
			[sg.Input(key='-YN4-', default_text='9.8')],
			[sg.Input(key='-ZAN3N4-', default_text='1')],
			[sg.Input(key='-ZBN3N4-', default_text='13')],
			[sg.Input(key='-ZN3-', default_text='4.2')],
			[sg.Input(key='-ZN4-', default_text='9.8')],
			[sg.Input(key='-YAN5-', default_text='1')],
			[sg.Input(key='-YBN5-', default_text='6.4')],
			[sg.Input(key='-YN5-', default_text='4.2')],
			[sg.Input(key='-ZAN5-', default_text='1')],
			[sg.Input(key='-ZBN5-', default_text='6.4')],
			[sg.Input(key='-ZN5-', default_text='4.2')],
			[sg.HorizontalSeparator()],
			[sg.Button('Exit')]
			]

layout_l = [[sg.Text('BASIC')],
			[sg.Text('Speed Reduction (n2)')],
			[sg.Text('Speed Reduction (n3)')],
			[sg.Text('Speed Reduction (n4)')],
			[sg.Text('Speed Reduction (n5)')],
			[sg.Text('Gear Module (n2 - n3)')],
			[sg.Text('Gear Module (n4 - n5)')],
			[sg.Text('Normal Diametral Pitch (T/in)')],
			[sg.Text('Velocity n2 (ft/min)')],
			[sg.Text('Velocity n3 (ft/min)')],
			[sg.Text('Velocity n4 (ft/min)')],
			[sg.Text('Velocity n5 (ft/min)')],
			[sg.Text('Power n2 (hp)')],
			[sg.Text('Power n3 (hp)')],
			[sg.Text('Power n4 (hp)')],
			[sg.Text('Power n5 (hp)')],
			[sg.Text('Power Delivered n2-n3 (lbf)')],
			[sg.Text('Power Delivered n4-n5 (lbf)')],
			[sg.HorizontalSeparator()],
			[sg.Text('BENDING N2-N3')],
			[sg.Text('Transverse Circular Pitch (T/in)')],
			[sg.Text('B Value')],
			[sg.Text('A Value')],
			[sg.Text('Velocity Factor Kv')],
			[sg.Text('Bending Stress P (psi)')],
			[sg.Text('Bending Stress G (psi)')],
			[sg.Text('Bending Strength (psi)')],
			[sg.Text('Stress Cycle Factor P')],
			[sg.Text('Stress Cycle Factor G')],
			[sg.Text('Bending Endurance Strength P (psi)')],
			[sg.Text('Bending Endurance Strength G (psi)')],
			[sg.Text('Safety Factor P (N2)')],
			[sg.Text('Safety Factor G (N3)')],
			[sg.Text('System Bending SF')],
			[sg.HorizontalSeparator()],
			[sg.Text('BENDING N4-N5')],
			[sg.Text('Transverse Circular Pitch (T/in)')],
			[sg.Text('B Value')],
			[sg.Text('A Value')],
			[sg.Text('Dynamic Factor KV')],
			[sg.Text('Bending Stress P (psi)')],
			[sg.Text('Bending Stress G (psi)')],
			[sg.Text('Bending Strength (psi)')],
			[sg.Text('Stress Cycle Factor P')],
			[sg.Text('Stress Cycle Factor G')],
			[sg.Text('Bending Endurance Strength P (psi)')],
			[sg.Text('Bending Endurance Strength G (psi)')],
			[sg.Text('Safety Factor P (N4)')],
			[sg.Text('Safety Factor G (N5)')],
			[sg.Text('System Bending SF')],
			[sg.HorizontalSeparator()],
			[sg.Text('WEAR N2-N3')],
			[sg.Text('Transverse Pressure Angle')],
			[sg.Text('Normal Circular Pitch (in)')],
			[sg.Text('Normal Base Pitch (in)')],
			[sg.Text('Pinion Pitch Circle Radius (in)')],
			[sg.Text('Gear Pitch Circle Radius (in)')],
			[sg.Text('Modifying Factor (a)')],
			[sg.Text('Pinion Base Circle Radius (in)')],
			[sg.Text('Gear Base Circle Radius (in)')],
			[sg.Text('A Value')],
			[sg.Text('B Value')],
			[sg.Text('C Value')],
			[sg.Text('Transverse Line of Action Z')],
			[sg.Text('Load Sharing Ratio (mN)')],
			[sg.Text('Geometry Factor I')],
			[sg.Text('Contact Stress (ksi)')],
			[sg.Text('Surface Endurance Strength (ksi)')],
			[sg.Text('Stress Cycle Factor P')],
			[sg.Text('Stress Cycle Factor G')],
			[sg.Text('Wear Stress P (ksi)')],
			[sg.Text('Wear Stress G (ksi)')],
			[sg.Text('Safety Factor P (N2)')],
			[sg.Text('Safety Factor G (N3)')],
			[sg.Text('System Wear SF')],
			[sg.Text('Overall System SF')],
			[sg.HorizontalSeparator()],
			[sg.Text('WEAR N4-N5')],
			[sg.Text('Transverse Pressure Angle')],
			[sg.Text('Normal Circular Pitch (in)')],
			[sg.Text('Normal Base Pitch (in)')],
			[sg.Text('Pinion Pitch Circle Radius (in)')],
			[sg.Text('Gear Pitch Circle Radius (in)')],
			[sg.Text('Modifying Factor (a)')],
			[sg.Text('Pinion Base Circle Radius (in)')],
			[sg.Text('Gear Base Circle Radius (in)')],
			[sg.Text('A Value')],
			[sg.Text('B Value')],
			[sg.Text('C Value')],
			[sg.Text('Transverse Line of Action Z')],
			[sg.Text('Load Sharing Ratio (mN)')],
			[sg.Text('Geometry Factor I')],
			[sg.Text('Contact Stress (ksi)')],
			[sg.Text('Surface Endurance Strength (ksi)')],
			[sg.Text('Stress Cycle Factor P')],
			[sg.Text('Stress Cycle Factor G')],
			[sg.Text('Wear Stress P (ksi)')],
			[sg.Text('Wear Stress G (ksi)')],
			[sg.Text('Safety Factor P (N4)')],
			[sg.Text('Safety Factor G (N5)')],
			[sg.Text('System Wear SF')],
			[sg.Text('Overall System SF')],
			[sg.HorizontalSeparator()],
			[sg.Text('SHAFT N2')],
			[sg.Text('Thrust Load Wa (lbf)')],
			[sg.Text('Radial Load Wr (lbf)')],
			[sg.Text('Total Force W (lbf)')],
			[sg.Text('Y - Forces to First Bearing A')],
			[sg.Text('Y - Forces to Second Bearing B')],
			[sg.Text('Y - Shear Force to First Bearing A')],
			[sg.Text('Y - Shear Force to Second Bearing B')],
			[sg.Text('Y - Thrust Load Moment N2 (lbf in)')],
			[sg.Text('Y - Sum of Moments N2 (lbf in)')],
			[sg.Text('Z - Forces to First Bearing A')],
			[sg.Text('Z - Forces to Second Bearing B')],
			[sg.Text('Z - Shear Force to First Bearing A')],
			[sg.Text('Z - Shear Force to Second Bearing B')],
			[sg.Text('Z - Transmitted Load Moment N2 (lbf in)')],
			[sg.Text('Z - Sum of Moments N2 (lbf in)')],
			[sg.Text('X - Forces in the Shaft')],
			[sg.HorizontalSeparator()],
			[sg.Text('SHAFT N3N4')],
			[sg.Text('Thrust Load Wa N3 (lbf)')],
			[sg.Text('Radial Load Wr N3 (lbf)')],
			[sg.Text('Total Force W N3 (lbf)')],
			[sg.Text('Thrust Load Wa N4 (lbf)')],
			[sg.Text('Radial Load Wr N4 (lbf)')],
			[sg.Text('Total Force W N4 (lbf)')],
			[sg.Text('Y - Forces to First Bearing A')],
			[sg.Text('Y - Forces to Second Bearing B')],
			[sg.Text('Y - Shear Force to First Bearing A')],
			[sg.Text('Y - Shear Force to Second Bearing B')],
			[sg.Text('Y - Thrust Load Moment N3 (lbf in)')],
			[sg.Text('Y - Thrust Load Moment N4 (lbf in)')],
			[sg.Text('Y - Sum of Moments N3N4 (lbf in)')],
			[sg.Text('Z - Forces to First Bearing A')],
			[sg.Text('Z - Forces to Second Bearing B')],
			[sg.Text('Z - Shear Force to First Bearing A')],
			[sg.Text('Z - Shear Force to Second Bearing B')],
			[sg.Text('Z - Thrust Load Moment N3 (lbf in)')],
			[sg.Text('Z - Thrust Load Moment N4 (lbf in)')],
			[sg.Text('Z - Sum of Moments N3N4 (lbf in)')],
			[sg.Text('X - Forces in the Shaft N3')],
			[sg.Text('X - Forces in the Shaft N4')],
			[sg.Text('X - Forces in the Shaft N3N4')],
			[sg.HorizontalSeparator()],
			[sg.Text('SHAFT N5')],
			[sg.Text('Thrust Load Wa (lbf)')],
			[sg.Text('Radial Load Wr (lbf)')],
			[sg.Text('Total Force W (lbf)')],
			[sg.Text('Y - Forces to First Bearing A')],
			[sg.Text('Y - Forces to Second Bearing B')],
			[sg.Text('Y - Shear Force to First Bearing A')],
			[sg.Text('Y - Shear Force to Second Bearing B')],
			[sg.Text('Y - Thrust Load Moment N5 (lbf in)')],
			[sg.Text('Y - Sum of Moments N5 (lbf in)')],
			[sg.Text('Z - Forces to First Bearing A')],
			[sg.Text('Z - Forces to Second Bearing B')],
			[sg.Text('Z - Shear Force to First Bearing A')],
			[sg.Text('Z - Shear Force to Second Bearing B')],
			[sg.Text('Z - Transmitted Load Moment N5 (lbf in)')],
			[sg.Text('Z - Sum of Moments N5 (lbf in)')],
			[sg.Text('X - Forces in the Shaft')],
			]

layout_p = [[sg.Text('VALUES')],
		  	[sg.Multiline(key='-SpeedReductionGearN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SpeedReductionGearN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SpeedReductionGearN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SpeedReductionGearN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SpeedReductionGearN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SpeedReductionGearN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-NormalDiametralPitch-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerDeliveredN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PowerDeliveredN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-TransverseCircularPN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BValueN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-AValueN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityFactorN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBendingStressPN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBendingStressGN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingStrengthN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorPN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorGN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingEndStrengthPN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingEndStrengthGN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorPN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorGN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SystemBendingSFN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-TransverseCircularPN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BValueN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-AValueN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-VelocityFactorN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBendingStressPN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBendingStressGN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingStrengthN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorPN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorGN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingEndStrengthPN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BendingEndStrengthGN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorPN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorGN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SystemBendingSFN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-TransversePressureAngleN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-NormalCircularPitchWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-NormalBasePitchWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PinionPitchCircleRadiusWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearPitchCircleRadiusWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ModifyingFactorWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PinionBaseCircleRadiusWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBaseCircleRadiusWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-AValueWearWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BValueWearWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-CValueWearWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TransverseLineZWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-LoadSharingRatioWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GeometryFactorWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ContactStressWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SurfaceEnduranceStrengthWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorPWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorGWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-WearStressPWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-WearStressGWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorPWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorGWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SystemWearWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-OverallSystemWearWN2N3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-TransversePressureAngleN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-NormalCircularPitchWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-NormalBasePitchWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PinionPitchCircleRadiusWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearPitchCircleRadiusWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ModifyingFactorWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-PinionBaseCircleRadiusWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GearBaseCircleRadiusWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-AValueWearWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-BValueWearWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-CValueWearWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TransverseLineZWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-LoadSharingRatioWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-GeometryFactorWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ContactStressWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SurfaceEnduranceStrengthWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorPWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-StressCycleFactorGWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-WearStressPWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-WearStressGWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorPWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SafetyFactorGWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-SystemWearWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-OverallSystemWearWN4N5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-ThrustLoadWaN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-RadialLoadWrN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TotalForceWN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesAN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesBN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceAN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceBN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YThrustLoadMomentN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YSumMomentsN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesAN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesBN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceAN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceBN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZThrustLoadMomentN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZSumMomentsN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-XForceInShaftN2-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-ThrustLoadWaN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-RadialLoadWrN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TotalForceWN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ThrustLoadWaN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-RadialLoadWrN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TotalForceWN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesAN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesBN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceAN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceBN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YThrustLoadMomentN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YThrustLoadMomentN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YSumMomentsN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesAN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesBN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceAN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceBN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZThrustLoadMomentN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZThrustLoadMomentN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZSumMomentsN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-XForceInShaftN3-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-XForceInShaftN4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-XForceInShaftN3N4-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.HorizontalSeparator()],
			[sg.Text('VALUES')],
			[sg.Multiline(key='-ThrustLoadWaN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-RadialLoadWrN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-TotalForceWN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesAN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YForcesBN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceAN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YShearForceBN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YThrustLoadMomentN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-YSumMomentsN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesAN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZForcesBN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceAN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZShearForceBN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZThrustLoadMomentN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-ZSumMomentsN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],
			[sg.Multiline(key='-XForceInShaftN5-', enter_submits=False, autoscroll=False, no_scrollbar=True )],

			]


layout_m = [[sg.Col(layout_l, p=0), sg.Col(layout_p, p=0)]]

layout = [
		[sg.Col(layout_t, p=0), sg.Col(layout_r, p=0), sg.Col(layout_m) ],
		]

layout_f = [[sg.Col(layout, scrollable=True, vertical_scroll_only=True, size_subsample_height=3)]]

window = sg.Window('Gear Calculations', layout_f, grab_anywhere=True, )

TV = 40

while True:
	event, values = window.read(timeout = TV)
	#print(event, values)
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	if event == 'Calculate':
		window['-SpeedReductionGearN2-'].update(float(values['-SteadyStateInput-'])*SpeedReductionGear(values['-FirstGearNT-'], values['-FirstGearNT-']))
		window['-SpeedReductionGearN3-'].update(float(values['-SteadyStateInput-'])*SpeedReductionGear(values['-FirstGearNT-'], values['-SecondGearNT-']))
		window['-SpeedReductionGearN4-'].update(float(values['-SteadyStateInput-'])*SpeedReductionGear(values['-FirstGearNT-'], values['-SecondGearNT-']))
		window['-SpeedReductionGearN5-'].update(float(values['-SteadyStateInput-'])*SpeedReductionGear(values['-FirstGearNT-'], values['-SecondGearNT-'])*SpeedReductionGear(values['-ThirdGearNT-'], values['-FourthGearNT-']))
		window['-SpeedReductionGearN2N3-'].update(SpeedReductionGears(values['-FirstGearNT-'], values['-SecondGearNT-']))
		window['-SpeedReductionGearN4N5-'].update(SpeedReductionGears(values['-ThirdGearNT-'], values['-FourthGearNT-']))
		window['-NormalDiametralPitch-'].update(NormalDiameterPitch([float(values['-FirstGearNT-']), float(values['-SecondGearNT-']), float(values['-ThirdGearNT-']), float(values['-FourthGearNT-'])], [float(values['-FirstGearPD-']), float(values['-SecondGearPD-']), float(values['-ThirdGearPD-']), float(values['-FourthGearPD-'])]))
		event, values = window.read(timeout = TV)
		window['-VelocityN2-'].update(Velocity(values['-FirstGearD-'], values['-SpeedReductionGearN2-']))
		window['-VelocityN3-'].update(Velocity(values['-SecondGearD-'], values['-SpeedReductionGearN3-']))
		window['-VelocityN4-'].update(Velocity(values['-ThirdGearD-'], values['-SpeedReductionGearN4-']))
		window['-VelocityN5-'].update(Velocity(values['-FourthGearD-'], values['-SpeedReductionGearN5-']))
		window['-PowerN2-'].update(Power(values['-Efficiency-'], values['-PowerOutput-'], 3)) # Decreasing Number of Gears
		window['-PowerN3-'].update(Power(values['-Efficiency-'], values['-PowerOutput-'], 2))
		window['-PowerN4-'].update(Power(values['-Efficiency-'], values['-PowerOutput-'], 1))
		window['-PowerN5-'].update(float(values['-PowerOutput-']))
		event, values = window.read(timeout = TV)
		window['-PowerDeliveredN2N3-'].update(PowerDelivered(values['-PowerN2-'], values['-VelocityN2-']))
		window['-PowerDeliveredN4N5-'].update(PowerDelivered(values['-PowerN4-'], values['-VelocityN4-']))
		window['-TransverseCircularPN2N3-'].update(TransverCircularP(values['-NormalDiametralPitch-'], values['-HelixAngle-']))
		window['-BValueN2N3-'].update(BValue(values['-QualityFactor-']))
		event, values = window.read(timeout = TV)
		window['-AValueN2N3-'].update(AValue(values['-BValueN2N3-']))
		event, values = window.read(timeout = TV)
		window['-VelocityFactorN2N3-'].update(VelocityFactor(values['-AValueN2N3-'], values['-BValueN2N3-'], values['-VelocityN3-']))
		event, values = window.read(timeout = TV)
		window['-GearBendingStressPN2N3-'].update(GearBendingStress(values['-PowerDeliveredN2N3-'], values['-OverloadFactor-'], values['-VelocityFactorN2N3-'], values['-SizeFactor-'], values['-TransverseCircularPN2N3-'], values['-FaceWidth-'], values['-LoadDistributionFactor-'], values['-RimThicknessFactor-'], values['-GeometryFactorJP-']))
		window['-GearBendingStressGN2N3-'].update(GearBendingStress(values['-PowerDeliveredN2N3-'], values['-OverloadFactor-'], values['-VelocityFactorN2N3-'], values['-SizeFactor-'], values['-TransverseCircularPN2N3-'], values['-FaceWidth-'], values['-LoadDistributionFactor-'], values['-RimThicknessFactor-'], values['-GeometryFactorJG-']))
		window['-BendingStrengthN2N3-'].update(BendingStrength(values['-SteelHardGrade-'], values['-HardnessBrinell-']))
		window['-StressCycleFactorPN2N3-'].update(StressCycleFactor(values['-LifeCycles-'], values['-SpeedReductionGearN2N3-'], 1)) # Pinion = 1
		window['-StressCycleFactorGN2N3-'].update(StressCycleFactor(values['-LifeCycles-'], values['-SpeedReductionGearN2N3-'], 2)) # Gear = 2
		event, values = window.read(timeout = TV)
		window['-BendingEndStrengthPN2N3-'].update(BendingEndStrength(values['-BendingStrengthN2N3-'], values['-SafetyFactor-'], values['-StressCycleFactorPN2N3-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		window['-BendingEndStrengthGN2N3-'].update(BendingEndStrength(values['-BendingStrengthN2N3-'], values['-SafetyFactor-'], values['-StressCycleFactorGN2N3-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		event, values = window.read(timeout = TV)
		window['-SafetyFactorPN2N3-'].update(SafetyFactor(values['-BendingEndStrengthPN2N3-'], values['-GearBendingStressPN2N3-']))
		window['-SafetyFactorGN2N3-'].update(SafetyFactor(values['-BendingEndStrengthGN2N3-'], values['-GearBendingStressGN2N3-']))
		event, values = window.read(timeout = TV)
		window['-SystemBendingSFN2N3-'].update(SystemSafetyFactor(values['-SafetyFactorPN2N3-'], values['-SafetyFactorGN2N3-']))
		window['-TransverseCircularPN4N5-'].update(TransverCircularP(values['-NormalDiametralPitch-'], values['-HelixAngle-']))
		window['-BValueN4N5-'].update(BValue(values['-QualityFactor-']))
		event, values = window.read(timeout = TV)
		window['-AValueN4N5-'].update(AValue(values['-BValueN4N5-']))
		event, values = window.read(timeout = TV)
		window['-VelocityFactorN4N5-'].update(VelocityFactor(values['-AValueN4N5-'], values['-BValueN4N5-'], values['-VelocityN5-']))
		event, values = window.read(timeout = TV)
		window['-GearBendingStressPN4N5-'].update(GearBendingStress(values['-PowerDeliveredN4N5-'], values['-OverloadFactor-'], values['-VelocityFactorN4N5-'], values['-SizeFactor-'], values['-TransverseCircularPN4N5-'], values['-FaceWidth-'], values['-LoadDistributionFactor-'], values['-RimThicknessFactor-'], values['-GeometryFactorJPN4N5-']))
		window['-GearBendingStressGN4N5-'].update(GearBendingStress(values['-PowerDeliveredN4N5-'], values['-OverloadFactor-'], values['-VelocityFactorN4N5-'], values['-SizeFactor-'], values['-TransverseCircularPN4N5-'], values['-FaceWidth-'], values['-LoadDistributionFactor-'], values['-RimThicknessFactor-'], values['-GeometryFactorJGN4N5-']))
		window['-BendingStrengthN4N5-'].update(BendingStrength(values['-SteelHardGrade-'], values['-HardnessBrinell-']))
		window['-StressCycleFactorPN4N5-'].update(StressCycleFactor(values['-LifeCycles-'], values['-SpeedReductionGearN4N5-'], 1)) # Pinion = 1
		window['-StressCycleFactorGN4N5-'].update(StressCycleFactor(values['-LifeCycles-'], values['-SpeedReductionGearN4N5-'], 2)) # Gear = 2
		event, values = window.read(timeout = TV)
		window['-BendingEndStrengthPN4N5-'].update(BendingEndStrength(values['-BendingStrengthN4N5-'], values['-SafetyFactor-'], values['-StressCycleFactorPN4N5-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		window['-BendingEndStrengthGN4N5-'].update(BendingEndStrength(values['-BendingStrengthN4N5-'], values['-SafetyFactor-'], values['-StressCycleFactorGN4N5-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		event, values = window.read(timeout = TV)
		window['-SafetyFactorPN4N5-'].update(SafetyFactor(values['-BendingEndStrengthPN4N5-'], values['-GearBendingStressPN4N5-']))
		window['-SafetyFactorGN4N5-'].update(SafetyFactor(values['-BendingEndStrengthGN4N5-'], values['-GearBendingStressGN4N5-']))
		event, values = window.read(timeout = TV)
		window['-SystemBendingSFN4N5-'].update(SystemSafetyFactor(values['-SafetyFactorPN4N5-'], values['-SafetyFactorGN4N5-']))
		window['-TransversePressureAngleN2N3-'].update(TransversePressure(values['-PressureAngle-'], values['-HelixAngle-']))
		window['-NormalCircularPitchWN2N3-'].update(NormalCircularPitch(values['-NormalDiametralPitch-']))
		event, values = window.read(timeout = TV)
		window['-NormalBasePitchWN2N3-'].update(NormalBasePitch(values['-NormalCircularPitchWN2N3-'], values['-PressureAngle-']))
		window['-PinionPitchCircleRadiusWN2N3-'].update(PitchCircleRadius(values['-FirstGearD-'], values['-SpeedReductionGearN2N3-'], 1))
		window['-GearPitchCircleRadiusWN2N3-'].update(PitchCircleRadius(values['-FirstGearD-'], values['-SpeedReductionGearN2N3-'], 2))
		window['-ModifyingFactorWN2N3-'].update(ModifyingFactor(values['-NormalDiametralPitch-']))
		event, values = window.read(timeout = TV)
		window['-PinionBaseCircleRadiusWN2N3-'].update(BaseCircleRadius(values['-PinionPitchCircleRadiusWN2N3-'], values['-TransversePressureAngleN2N3-'], values['-SpeedReductionGearN2N3-'], 1))
		window['-GearBaseCircleRadiusWN2N3-'].update(BaseCircleRadius(values['-PinionPitchCircleRadiusWN2N3-'], values['-TransversePressureAngleN2N3-'], values['-SpeedReductionGearN2N3-'], 2))
		event, values = window.read(timeout = TV)
		window['-AValueWearWN2N3-'].update(AValueWear(values['-ModifyingFactorWN2N3-'], values['-PinionPitchCircleRadiusWN2N3-'], values['-PinionBaseCircleRadiusWN2N3-']))
		window['-BValueWearWN2N3-'].update(BValueWear(values['-ModifyingFactorWN2N3-'], values['-GearPitchCircleRadiusWN2N3-'], values['-GearBaseCircleRadiusWN2N3-']))
		window['-CValueWearWN2N3-'].update(CValueWear(values['-PinionPitchCircleRadiusWN2N3-'], values['-GearPitchCircleRadiusWN2N3-'], values['-TransversePressureAngleN2N3-']))
		event, values = window.read(timeout = TV)
		window['-TransverseLineZWN2N3-'].update(TransverseLineZ(values['-AValueWearWN2N3-'], values['-BValueWearWN2N3-'], values['-CValueWearWN2N3-']))
		event, values = window.read(timeout = TV)
		window['-LoadSharingRatioWN2N3-'].update(LoadSharingRatio(values['-NormalBasePitchWN2N3-'], values['-TransverseLineZWN2N3-']))
		event, values = window.read(timeout = TV)
		window['-GeometryFactorWN2N3-'].update(GeometryFactorW(values['-TransversePressureAngleN2N3-'], values['-LoadSharingRatioWN2N3-'], values['-SpeedReductionGearN2N3-']))
		event, values = window.read(timeout = TV)
		window['-ContactStressWN2N3-'].update(ContactStressW(values['-ElasticCoefficient-'], values['-PowerDeliveredN2N3-'], values['-OverloadFactor-'], values['-VelocityFactorN2N3-'], values['-SizeFactor-'], values['-LoadDistributionFactor-'], values['-FirstGearD-'], values['-FaceWidth-'], values['-SurfaceConditionFactor-'], values['-GeometryFactorWN2N3-']) / 1000)
		window['-SurfaceEnduranceStrengthWN2N3-'].update(SurfaceEnduranceStrengthW(values['-HardnessBrinell-'], values['-SteelHardGrade-']) / 1000)
		window['-StressCycleFactorPWN2N3-'].update(StressCycleFactorWear(values['-LifeCycles-'], values['-SpeedReductionGearN2N3-'], 1))
		window['-StressCycleFactorGWN2N3-'].update(StressCycleFactorWear(values['-LifeCycles-'], values['-SpeedReductionGearN2N3-'], 2))
		event, values = window.read(timeout = TV)
		window['-WearStressPWN2N3-'].update(WearStress(values['-SurfaceEnduranceStrengthWN2N3-'], values['-StressCycleFactorPWN2N3-'], values['-HardnessRatioFactorWear-'], values['-SafetyFactorWear-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		window['-WearStressGWN2N3-'].update(WearStress(values['-SurfaceEnduranceStrengthWN2N3-'], values['-StressCycleFactorGWN2N3-'], values['-HardnessRatioFactorWear-'], values['-SafetyFactorWear-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		event, values = window.read(timeout = TV)
		window['-SafetyFactorPWN2N3-'].update(SafetyFactorWear(values['-WearStressPWN2N3-'], values['-ContactStressWN2N3-']))
		window['-SafetyFactorGWN2N3-'].update(SafetyFactorWear(values['-WearStressGWN2N3-'], values['-ContactStressWN2N3-']))
		event, values = window.read(timeout = TV)
		window['-SystemWearWN2N3-'].update(SystemWear(values['-SafetyFactorPWN2N3-'], values['-SafetyFactorGWN2N3-']))
		window['-OverallSystemWearWN2N3-'].update(OverallSystemWear(values['-SafetyFactorPWN2N3-'], values['-SafetyFactorGWN2N3-'], values['-SafetyFactorPN2N3-'], values['-SafetyFactorGN2N3-']))
		window['-TransversePressureAngleN4N5-'].update(TransversePressure(values['-PressureAngle-'], values['-HelixAngle-']))
		window['-NormalCircularPitchWN4N5-'].update(NormalCircularPitch(values['-NormalDiametralPitch-']))
		event, values = window.read(timeout = TV)
		window['-NormalBasePitchWN4N5-'].update(NormalBasePitch(values['-NormalCircularPitchWN4N5-'], values['-PressureAngle-']))
		window['-PinionPitchCircleRadiusWN4N5-'].update(PitchCircleRadius(values['-ThirdGearD-'], values['-SpeedReductionGearN4N5-'], 1))
		window['-GearPitchCircleRadiusWN4N5-'].update(PitchCircleRadius(values['-ThirdGearD-'], values['-SpeedReductionGearN4N5-'], 2))
		window['-ModifyingFactorWN4N5-'].update(ModifyingFactor(values['-NormalDiametralPitch-']))
		event, values = window.read(timeout = TV)
		window['-PinionBaseCircleRadiusWN4N5-'].update(BaseCircleRadius(values['-PinionPitchCircleRadiusWN4N5-'], values['-TransversePressureAngleN4N5-'], values['-SpeedReductionGearN4N5-'], 1))
		window['-GearBaseCircleRadiusWN4N5-'].update(BaseCircleRadius(values['-PinionPitchCircleRadiusWN4N5-'], values['-TransversePressureAngleN4N5-'], values['-SpeedReductionGearN4N5-'], 2))
		event, values = window.read(timeout = TV)
		window['-AValueWearWN4N5-'].update(AValueWear(values['-ModifyingFactorWN4N5-'], values['-PinionPitchCircleRadiusWN4N5-'], values['-PinionBaseCircleRadiusWN4N5-']))
		window['-BValueWearWN4N5-'].update(BValueWear(values['-ModifyingFactorWN4N5-'], values['-GearPitchCircleRadiusWN4N5-'], values['-GearBaseCircleRadiusWN4N5-']))
		window['-CValueWearWN4N5-'].update(CValueWear(values['-PinionPitchCircleRadiusWN4N5-'], values['-GearPitchCircleRadiusWN4N5-'], values['-TransversePressureAngleN4N5-']))
		event, values = window.read(timeout = TV)
		window['-TransverseLineZWN4N5-'].update(TransverseLineZ(values['-AValueWearWN4N5-'], values['-BValueWearWN4N5-'], values['-CValueWearWN4N5-']))		
		event, values = window.read(timeout = TV)
		window['-LoadSharingRatioWN4N5-'].update(LoadSharingRatio(values['-NormalBasePitchWN4N5-'], values['-TransverseLineZWN4N5-']))
		event, values = window.read(timeout = TV)
		window['-GeometryFactorWN4N5-'].update(GeometryFactorW(values['-TransversePressureAngleN4N5-'], values['-LoadSharingRatioWN4N5-'], values['-SpeedReductionGearN4N5-']))
		event, values = window.read(timeout = TV)
		window['-ContactStressWN4N5-'].update(ContactStressW(values['-ElasticCoefficient-'], values['-PowerDeliveredN4N5-'], values['-OverloadFactor-'], values['-VelocityFactorN4N5-'], values['-SizeFactor-'], values['-LoadDistributionFactor-'], values['-ThirdGearD-'], values['-FaceWidth-'], values['-SurfaceConditionFactor-'], values['-GeometryFactorWN4N5-']) / 1000)
		window['-SurfaceEnduranceStrengthWN4N5-'].update(SurfaceEnduranceStrengthW(values['-HardnessBrinell-'], values['-SteelHardGrade-']) / 1000)
		window['-StressCycleFactorPWN4N5-'].update(StressCycleFactorWear(values['-LifeCycles-'], values['-SpeedReductionGearN4N5-'], 1))
		window['-StressCycleFactorGWN4N5-'].update(StressCycleFactorWear(values['-LifeCycles-'], values['-SpeedReductionGearN4N5-'], 2))
		event, values = window.read(timeout = TV)
		window['-WearStressPWN4N5-'].update(WearStress(values['-SurfaceEnduranceStrengthWN4N5-'], values['-StressCycleFactorPWN4N5-'], values['-HardnessRatioFactorWear-'], values['-SafetyFactorWear-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		window['-WearStressGWN4N5-'].update(WearStress(values['-SurfaceEnduranceStrengthWN4N5-'], values['-StressCycleFactorGWN4N5-'], values['-HardnessRatioFactorWear-'], values['-SafetyFactorWear-'], values['-TemperatureFactor-'], values['-ReliabilityFactor-']))
		event, values = window.read(timeout = TV)
		window['-SafetyFactorPWN4N5-'].update(SafetyFactorWear(values['-WearStressPWN4N5-'], values['-ContactStressWN4N5-']))
		window['-SafetyFactorGWN4N5-'].update(SafetyFactorWear(values['-WearStressGWN4N5-'], values['-ContactStressWN4N5-']))
		event, values = window.read(timeout = TV)
		window['-SystemWearWN4N5-'].update(SystemWear(values['-SafetyFactorPWN4N5-'], values['-SafetyFactorGWN4N5-']))
		window['-OverallSystemWearWN4N5-'].update(OverallSystemWear(values['-SafetyFactorPWN4N5-'], values['-SafetyFactorGWN4N5-'], values['-SafetyFactorPN4N5-'], values['-SafetyFactorGN4N5-']))

	
		window['-ThrustLoadWaN2-'].update()
		window['-RadialLoadWrN2-'].update()
		window['-TotalForceWN2-'].update()
		window['-YForcesAN2-'].update()
		window['-YForcesBN2-'].update()
		window['-YShearForceAN2-'].update()
		window['-YShearForceBN2-'].update()
		window['-YThrustLoadMomentN2-'].update()
		window['-YSumMomentsN2-'].update()
		window['-ZForcesAN2-'].update()
		window['-ZForcesBN2-'].update()
		window['-ZShearForceAN2-'].update()
		window['-ZShearForceBN2-'].update()
		window['-ZThrustLoadMomentN2-'].update()
		window['-ZSumMomentsN2-'].update()
		window['-XForceInShaftN2-'].update()
		[sg.HorizontalSeparator()],
		[sg.Text('VALUES')],
		window['-ThrustLoadWaN3-'].update()
		window['-RadialLoadWrN3-'].update()
		window['-TotalForceWN3-'].update()
		window['-ThrustLoadWaN4-'].update()
		window['-RadialLoadWrN4-'].update()
		window['-TotalForceWN4-'].update()
		window['-YForcesAN3N4-'].update()
		window['-YForcesBN3N4-'].update()
		window['-YShearForceAN3N4-'].update()
		window['-YShearForceBN3N4-'].update()
		window['-YThrustLoadMomentN3-'].update()
		window['-YThrustLoadMomentN4-'].update()
		window['-YSumMomentsN3N4-'].update()
		window['-ZForcesAN3N4-'].update()
		window['-ZForcesBN3N4-'].update()
		window['-ZShearForceAN3N4-'].update()
		window['-ZShearForceBN3N4-'].update()
		window['-ZThrustLoadMomentN3-'].update()
		window['-ZThrustLoadMomentN4-'].update()
		window['-ZSumMomentsN3N4-'].update()
		window['-XForceInShaftN3-'].update()
		window['-XForceInShaftN4-'].update()
		window['-XForceInShaftN3N4-'].update()
		[sg.HorizontalSeparator()],
		[sg.Text('VALUES')],
		window['-ThrustLoadWaN5-'].update()
		window['-RadialLoadWrN5-'].update()
		window['-TotalForceWN5-'].update()
		window['-YForcesAN5-'].update()
		window['-YForcesBN5-'].update()
		window['-YShearForceAN5-'].update()
		window['-YShearForceBN5-'].update()
		window['-YThrustLoadMomentN5-'].update()
		window['-YSumMomentsN5-'].update()
		window['-ZForcesAN5-'].update()
		window['-ZForcesBN5-'].update()
		window['-ZShearForceAN5-'].update()
		window['-ZShearForceBN5-'].update()
		window['-ZThrustLoadMomentN5-'].update()
		window['-ZSumMomentsN5-'].update()
		window['-XForceInShaftN5-'].update()

window.close()

