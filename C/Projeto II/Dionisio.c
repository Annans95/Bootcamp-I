#include <stdio.h>
#include <locale.h>
int main (){
    setlocale(LC_ALL, "Portuguese");
    float v1=0;
    float v2=0;
    int operacao=0;
printf("Digite o primeiro valor:");
scanf("%f", &v1);
printf("Digite o segundo valor:");
scanf("%f", &v2);
printf("Escolha uma das opera��es abaixo digitando seu menu:\n");
printf("1-soma\n");
printf("2-subtra��o\n");
printf("3-multiplica��o\n");
printf("4-divis�o\n");
printf("Digite aqui a op��o desejada:");
scanf("%i", &operacao);
switch (operacao){
case 1:
    printf("A Soma dos valores �:%.2f\n",v1+v2);
    break;
case 2:
    printf("A Substra��o dos valores �:%.2f\n",v1-v2);
    break;
case 3:
    printf("A Multiplica��o dos valores �:%.2f\n",v1*v2);
    break;
case 4:
    printf("A Divis�o dos valores �:%.2f\n",v1/v2);
    break;
default:
    printf("Opera��o inv�lida");
}
return 0;
}

