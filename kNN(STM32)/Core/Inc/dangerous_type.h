/*
 * dangerous.h
 *
 *  Created on: 2020年12月15日
 *      Author: Gordon_Zhuang
 */

#ifndef INC_DANGEROUS_TYPE_H_
#define INC_DANGEROUS_TYPE_H_

#define behavior_type(arg) \
	char* drive_type;\
    if (arg == 0){\
    	drive_type = "normal"; \
    } else if (arg == 1){ \
    	drive_type = "lane_change"; \
    } else if (arg == 2){ \
    	drive_type = "breaking"; \
    }

#endif /* INC_DANGEROUS_TYPE_H_ */
