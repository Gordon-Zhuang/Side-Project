/*
 * ACC_BREAK.cpp
 *
 *  Created on: 2021年2月1日
 *      Author: Gordon_Zhuang
 */
#include<iostream>
#include<cstdlib>
#include<math.h>
#include<drive.h>
int Acc_Break(float x = 0.15){
///////////////////////////////////////////////////////
	/*建立模糊子集*/
///////////////////////////////////////////////////////
	CTrapezoi_fuzzy XL;//X負值過高子集
	CTrapezoi_fuzzy XM;//X正常子集
	CTrapezoi_fuzzy XH;//X過高子集
	/*XL*/
	XL.a = -1;
	XL.m = -1;
	XL.n = -0.4;
	XL.d = -0.1;
	/*XM*/
	XM.a = -0.25;
	XM.m = 0;
	XM.n = 0;
	XM.d = 0.25;
	/*XH*/
	XH.a = 0.1;
	XH.m = 0.4;
	XH.n = 1;
	XH.d = 1;
///////////////////////////////////////////////////////
	/*建立解模糊結果*/
///////////////////////////////////////////////////////
	CTrapezoi_defuzzy SL;//減速過高子集
	CTrapezoi_defuzzy SM;//速度正常子集
	CTrapezoi_defuzzy SH;//加速過高子集
	/*SL*/
	SL.a = -1;
	SL.m = -1;
	SL.n = -0.8;
	SL.d = -0.4;
	/*SM*/
	SM.a = -0.4;
	SM.m = 0;
	SM.n = 0;
	SM.d = 0.4;
	/*SH*/
	SH.a = 0.4;
	SH.m = 0.8;
	SH.n = 1;
	SH.d = 1;
///////////////////////////////////////////////////////
	/*模糊化以及套用模糊規則*/
	/*最大最小合成法*/
///////////////////////////////////////////////////////
	float temp = 0;
	if (XL.a < x and x < XL.d){   //// XL子集(X負值過高)
		temp = XL.hight(x);
		SL.high = max(SL.high,temp);
	}
	if(XM.a < x and x < XM.d){    ////XM子集(X正常)
		temp = XM.hight(x);
		SM.high = max(SM.high,temp);
	}
	if (XH.a < x and x < XH.d){    ////XH子集(X過高)
		temp = XH.hight(x);
		SH.high = max(SH.high,temp);
	}
///////////////////////////////////////////////////
	/*解模糊*/
///////////////////////////////////////////////////
	float ans = 0;
	float area = 0;
	ans += SL.integral();
	ans += SM.integral();
	ans += SH.integral();
	area += SL.area();
	area += SM.area();
	area += SH.area();
	ans /= area;
	return ans;
}
