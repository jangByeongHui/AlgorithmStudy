#include <stdio.h>
#include <stdlib.h>

struct offer{
	int size;
	int price;
	int id;
};
struct scenario{
	int target_revenue;
	int targetID;
	int size;
};

struct offer *sorted_offer;
struct scenario *sorted_scenario;
//flag 0:offer 1:scenario
void merge_offer_sort(struct offer *list, int left, int right);
void merge_offer(struct offer *list, int left, int mid, int right);
void merge_scenario_sort(struct scenario *list, int left, int right,int flag);
void merge_scenario(struct scenario *list, int left, int mid, int right,int flag);
void offer_add(int* s, struct offer **ar);


int main(void)
{
	struct offer *offer;
	struct scenario *scenario;
	int N,numBuyer,numScenario,offer_len=0;
	
	scanf("%d",&N);
	//소비자 제안 입력
	for(int i=0;i<N;i++){
		scanf("%d",&numBuyer);

		for(int j=0;j<numBuyer;j++){
			struct offer temp;
			temp.id=i;
			scanf("%d",&temp.size);
			scanf("%d",&temp.price);
			offer_add(&offer_len,&offer);
			offer[offer_len-1]=temp;
		}

	}
	// for(int i=0;i<offer_len;i++){
	// 	printf("offer_size: %d offer_price: %d offer_id: %d\n",offer[i].size,offer[i].price,offer[i].id);
	// }
	//size 별로 제안 금액 정렬
	sorted_offer=(struct offer*)malloc(sizeof(struct offer)*offer_len);
	// for(int i=0;i<offer_len;i++){
	// 	printf("%d %d %d\n",offer[i].size,offer[i].price,offer[i].id);
	// }
	merge_offer_sort(offer,0,offer_len-1);
	// for(int i=0;i<offer_len;i++){
	// 	printf("offer_size: %d offer_price: %d offer_id: %d\n",offer[i].size,offer[i].price,offer[i].id);
	// }
	free(sorted_offer);
	//목표 매출액 입력
	scanf("%d",&numScenario);
	scenario=(struct scenario*)malloc(sizeof(struct scenario)*numScenario);
	sorted_scenario=(struct scenario*)malloc(sizeof(struct scenario)*numScenario);

	for(int i=0;i<numScenario;i++){
		struct scenario temp;
		scanf("%d",&temp.target_revenue);
		temp.targetID=i+1;
		scenario[i]=temp;
	}
	//목표 매출액 별로 시나리오 정렬
	merge_scenario_sort(scenario,0,numScenario-1,0);
	// for(int i=0;i<offer_len;i++){
	// 	printf("%d %d \n",scenario[i].target_revenue,scenario[i].targetID);
	// }

	//calculate
	int revenue=0;
	int *buyerPayment=(int*)malloc(sizeof(int)*(N+1));
	for(int i=0;i<N+1;i++){
		buyerPayment[i]=0;
	}
	int sIndex=0;
	for(int i=0;i<offer_len;i++){
		int size=offer[i].size;
		int payment=offer[i].price;
		int buyerID=offer[i].id;

		if(payment>buyerPayment[buyerID]){
			revenue+=-buyerPayment[buyerID]+payment;
			buyerPayment[buyerID]=payment;
		}
		// printf("size:%d revenue : %d \n",size,revenue);
		while(sIndex<numScenario && scenario[sIndex].target_revenue<=revenue){	
			scenario[sIndex].size=size;
			sIndex++;
		}
	}
	while(sIndex<numScenario){
		scenario[sIndex].size=-1;
		sIndex++;
	}
	merge_scenario_sort(scenario,0,numScenario-1,1);
	for(int i=0;i<numScenario;i++){
		printf("%d ",scenario[i].size);
	}
	free(scenario);
	free(offer);
	free(sorted_scenario);
	
	return 0;
}


void offer_add(int* s, struct offer **ar){
    int newsize = *s + 1; //size의 크기를 1 증가시킴

    //main의 arr보다 길이가 긴 배열 생성
	struct offer* temp = (struct offer*)malloc(sizeof(struct offer)*newsize);
    //ar의 값을 temp에 복사
    for (int i = 0; i < *s; i++)
    	temp[i] = (*ar)[i];
	if(*s>0)
    	free(*ar); //이전 배열 삭제
    *ar = temp;
    *s += 1; //main의 size를 1증가시킴
}

void merge_offer(struct offer *list, int left, int mid, int right){
  int i, j, k, l;
  i = left;
  j = mid+1;
  k = left;

  /* 분할 정렬된 list의 합병 */
  while(i<=mid && j<=right){
    if(list[i].size<=list[j].size)
      sorted_offer[k++] = list[i++];
    else
      sorted_offer[k++] = list[j++];
  }

  // 남아 있는 값들을 일괄 복사
  if(i>mid){
    for(l=j; l<=right; l++)
      sorted_offer[k++] = list[l];
  }
  // 남아 있는 값들을 일괄 복사
  else{
    for(l=i; l<=mid; l++)
      sorted_offer[k++] = list[l];
  }

  // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
  for(l=left; l<=right; l++){
    list[l] = sorted_offer[l];
  }
}

// 합병 정렬
void merge_offer_sort(struct offer *list, int left, int right){
  int mid;

  if(left<right){
    mid = (left+right)/2; // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
    merge_offer_sort(list, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
    merge_offer_sort(list, mid+1, right); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
    merge_offer(list, left, mid, right); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
  }
}
//key에 따른 정렬 flag 0:revenue 1:id
void merge_scenario(struct scenario *list, int left, int mid, int right,int flag){
  int i, j, k, l;
  i = left;
  j = mid+1;
  k = left;

  /* 분할 정렬된 list의 합병 */
  while(i<=mid && j<=right){
	if(flag){
		if(list[i].targetID<=list[j].targetID)
      		sorted_scenario[k++] = list[i++];
    	else
      		sorted_scenario[k++] = list[j++];
	}else{
		if(list[i].target_revenue<=list[j].target_revenue)
      		sorted_scenario[k++] = list[i++];
    	else
      		sorted_scenario[k++] = list[j++];
	}
    
  }

  // 남아 있는 값들을 일괄 복사
  if(i>mid){
    for(l=j; l<=right; l++)
      sorted_scenario[k++] = list[l];
  }
  // 남아 있는 값들을 일괄 복사
  else{
    for(l=i; l<=mid; l++)
      sorted_scenario[k++] = list[l];
  }

  // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
  for(l=left; l<=right; l++){
    list[l] = sorted_scenario[l];
  }
}

// 합병 정렬
void merge_scenario_sort(struct scenario *list, int left, int right,int flag){
  int mid;

  if(left<right){
    mid = (left+right)/2; // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
    merge_scenario_sort(list, left, mid,flag); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
    merge_scenario_sort(list, mid+1, right,flag); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
    merge_scenario(list, left, mid, right,flag); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
  }
}

