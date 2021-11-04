/*
 * drive.h
 *
 *  Created on: 2021年1月28日
 *      Author: Gordon_Zhuang
 */

#ifndef INC_DRIVE_H_
#define INC_DRIVE_H_

int Drive_Behavior(float IMU);

float max(float x, float y);

int Acc_Break(float x);

class CTrapezoi_defuzzy{
	public:
		float a,m,n,d;
		float high = 0;
		float integral(void);
		float area(void);
	private:
		float slopem;
		float slopen;
		float mp;
		float np;
};
class CTrapezoi_fuzzy{
	public:
		float a,m,n,d;
		float hight(float x);
};


#endif /* INC_DRIVE_H_ */
