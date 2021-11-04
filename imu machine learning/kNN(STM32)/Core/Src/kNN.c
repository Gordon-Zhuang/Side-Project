
#include "stdio.h"
#include "model.h"
#include "dangerous_type.h"
#include "math.h"
char* kNN(float test_data[], int k){

	float distance[7525][2];
	for (int i = 0; i < 7525; i++) {
		float  temp = 0;
		for (int j = 0; j < 5; j++) {
			temp += pow(model_lan_break[i][j] - test_data[j], 2);
		}
		temp = sqrt(temp);
		distance[i][0] = temp;
		distance[i][1] = model_lan_break[i][5];
	}
	partition(0,7524,distance, k);
	int ans = kvote(distance,k);
	behavior_type(ans)
	return drive_type;
}
int partition(int start,int end, float distance[][2], int k){
	if (start == end){
		return 0;
	}
	int left = start;
	int right = end;
	float pvoid = distance[(start+end)/2][0];
	while(left <= right){
		if(distance[left][0] < pvoid){
			left += 1;
			continue;
		}
		if(distance[right][0] > pvoid){
			right -= 1;
			continue;
		}
		float temp = distance[left][0];
		distance[left][0] = distance[right][0];
		distance[right][0] = temp;
		temp = distance[left][1];
		distance[left][1] = distance[right][1];
		distance[right][1] = temp;
		left += 1;
		right -= 1;
	}
	if (k <= right){
		partition(start,right,distance,k);
	}
	if (k >= left){
		partition(left,end,distance,k);
	}
	return 0;
}
int kvote(float distance[][2], int k){
	int label[] = {0,0,0};
	for(int i = 0; i < k ; i++){
		int temp = distance[i][1];
		label[temp] ++;
	}
	int temp = 0;
	int ans = 0;
	for(int i = 0; i < 3 ; i++){
		if (label[i] > temp){
			temp = label[i];
			ans = i;
		}
	}
	return ans;
}
