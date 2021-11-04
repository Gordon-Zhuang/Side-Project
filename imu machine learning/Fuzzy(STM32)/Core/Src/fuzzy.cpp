/*
 * defuzzy.cpp
 *
 *  Created on: 2021年1月29日
 *      Author: Gordon_Zhuang
 */
#include<drive.h>
#include<math.h>
float CTrapezoi_defuzzy::integral(void){
	float left = 0;
	float mid = 0;
	float right = 0;
	float all = 0;
	slopem = 1/(m-a);
	slopen = -1/(d-n);
	mp = a + (m-a)*(high/1);
	np = d - (d-n)*(high/1);
	///////left:slopem*(x-a)*x dx/slopem*(x-a) dx
	//== [slopem*((1/3)*x^3-(1/2)*a*x^2)/slopem*((1/2)X^2-ax)]//////////////////
	if (isnormal(slopem)){
		left = slopem*((mp*mp*mp/3)-(a*mp*mp/2))-slopem*((a*a*a/3)-(a*a*a/2));
	}
	///////mid://////
	mid = (high*np*np/2-high*mp*mp/2);
	//////right//////
	if (isnormal(slopen)){
		right = slopen*(d*d*d/3-d*d*d/2)-slopen*(np*np*np/3-d*np*np/2);
	}
	//////all//////

	all = (left + mid + right);
	return all;
}
float CTrapezoi_defuzzy::area(void){
	float area;
	mp = a + (m-a)*(high/1);
	np = d - (d-n)*(high/1);
	area = ((np-mp)+(d-a))*high/2;
	return area;
}
float CTrapezoi_fuzzy::hight(float x){
	if (a < x and x < m){
		return (x-a)/(m-a);
	}
	else if (m < x and x < n){
		return 1;
	}
	else if (n < x and x < d){
		return (d-x)/(d-n);
	}
}
