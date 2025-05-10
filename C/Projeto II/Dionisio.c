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
printf("Escolha uma das operações abaixo digitando seu menu:\n");
printf("1-soma\n");
printf("2-subtração\n");
printf("3-multiplicação\n");
printf("4-divisão\n");
printf("Digite aqui a opção desejada:");
scanf("%i", &operacao);
switch (operacao){
case 1:
    printf("A Soma dos valores é:%.2f\n",v1+v2);
    break;
case 2:
    printf("A Substração dos valores é:%.2f\n",v1-v2);
    break;
case 3:
    printf("A Multiplicação dos valores é:%.2f\n",v1*v2);
    break;
case 4:
    printf("A Divisão dos valores é:%.2f\n",v1/v2);
    break;
default:
    printf("Operação inválida");
}
return 0;
}

