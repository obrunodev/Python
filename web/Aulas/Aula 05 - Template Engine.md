# Aula 05 - Template Engine

Template engine, é uma ferramenta dentro da biblioteca flask que nos permite renderizar páginas dinamicamente.

Para que o flask entenda o momento certo de agir, devemos utilizar o sinal "{{ Código aqui }}".

Para fazermos um teste, basta inserir um {{ 5 + 4 }} dentro do body do HTML e executar o servidor, ao abrir, será mostrado o número 9, resultado da soma entre 5 e 4.

```html
<body>

  <!--Ao executar em flask, a página mostrará o resultado da operação dentro do sinal "{{}}"-->
  {{ 5 + 4 }} 

</body>
```

Nessa aula apenas mostrei como utilizar o HTML de forma mais dinamica com o flask. partiremos agora para alguns parâmetros URL.