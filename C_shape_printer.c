#include <stdio.h>
#include <string.h>
 int col, rows, n, t, p;
 char k;


char rhombus[] = "rhombus";
char triangle[] = "triangle";
char pascals_pyramid[] = "pascals_pyramid";
char pyramid[] = "pyramid";
char users_choice[100];


int rhombuss();
int pascals_pyramidd();
int trianglee();
int pyramidd();


int main(){ 
  int result;

   
    choose_shape:
   printf("please choose a shape :\n 1 - rhombus\n 2 - triangle\n 3 - pascals_pyramid\n");
      scanf("%s", &users_choice);
      
result = strcmp(users_choice, triangle);

  if((result = strcmp(users_choice, rhombus)==0)){    
   rhombuss();}
   else if((result = strcmp(users_choice, triangle)==0)){    
   trianglee();}
   else if((result = strcmp(users_choice, pascals_pyramid)==0)){    
   pascals_pyramidd();}
   else if((result = strcmp(users_choice, pyramid)==0)){    
   pyramidd();}
   else{ printf("invalid choice, try again.\n\n\n");
    goto choose_shape;
}
}



int pascals_pyramidd(){
int c, i, j ,k;

printf("please enter the number of rows : ");
scanf("%d", &rows);


for( i=0; i<rows; i++){

   for( j=0; j<rows-i; j++)
   printf(" ");

   for(k=0; k<=i; k++){
      if(k == 0||i ==0)
      c = 1;
      
      else 
      c = c * (i-k+1)/k;

   
      printf("%d ", c);
   }

   
   printf("\n");


}
}

int rhombuss(){
char upperletter[5];
char lowerletter[5];
int compare;
char userss[10];
char decend[]="decending";
char acend[]="acending";
 

printf("input the amount of rows : ");

    scanf("%d", &n); 

printf("please enter the chosen letter for the upper half : ");

    scanf("%s", &upperletter);

printf("please enter the chosen letter for the lower half : ");

    scanf("%s", &lowerletter);

 for(rows=1; rows<=n; rows++){
   
   for(col=1; col<=n-rows; col++){
          printf(" ");}
   
   for(col=1; col<=rows; col++ ){
          printf("%s ", upperletter); }
   
    printf("\n");
   }
   
   for(rows=n; rows>0; rows--)
   {

      for(col=1; col<=n-rows; col++)
          printf(" ");

      for(col=rows; col>=1; col-- )
          printf("%s ", lowerletter); 

   printf("\n");
   }
}

int trianglee(){

  char left[]="left";
  char right[]="right";
  char user[30];
  int result;

   printf ("enter the number of rows :");
   scanf("%d", &rows);
printf("what direction would you like the triangle to face? \n left    right\n");
scanf("%s", &user);
   if((result = strcmp(user,right)) == 0){
   for(int i = 1; i <rows; i++){
      for(int j = 0; j < i; j++){
         printf("^");
      }
 printf("\n");  }
} else if((result = strcmp(user,left)) == 0){

for(int i=0; i<rows; i++){

    for (int spc = 0; spc<rows-i ; spc++)
    {
        printf(" ");
    }
    
    for (int d = 0; d < i; d++)
    {
        printf("^");


    }
    printf("\n");
}

}
}

int pyramidd(){

printf("please enter the size (rows) of the pyramid : \n");
scanf("%d", &rows);

printf("please enter the chosen letter/number to represent the pyramid : ");
scanf("%c", &k);

for(int i = 0; i<rows; i++){

    for(int spc= 0; spc < rows-i; spc++)
    printf(" ");

    for(int j=0; j<i; j++)
    printf("%c ", k);

  printf("\n");  
}



}




   

