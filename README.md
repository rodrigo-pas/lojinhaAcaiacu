# 🍧 Lojinha AÇAIAÇU – Sistema de Pedidos (Python)
Este programinha simula o sistema de pedidos da **Lojinha AÇAIAÇU**, permitindo ao cliente escolher entre os sabores *açaí* ou *cupuaçu*, nos tamanhos *P, M ou G*. O pedido é feito via console, com repetição até o cliente finalizar a compra.

## 💻 Tecnologias utilizadas
- Linguagem Python
- Terminal/Console

## ⚙️ Funcionalidades
- Cardápio exibido no início com preços por sabor e tamanho
- Escolha entre dois sabores: Açaí (AC) ou Cupuaçu (CP)
- Três tamanhos disponíveis: Pequeno (P), Médio (M), Grande (G)
- Loop para adicionar vários pedidos
- Cálculo automático do total da compra
- Validação de entradas para evitar opções inválidas

## ▶️ Como executar
1. Copie o código para um arquivo `.py`, por exemplo `lojinha.py`.
2. Execute com Python 3 em seu terminal:
```bash
python lojinha.py
```

## 📝 Exemplo de uso:
```bash
Por favor, escolha (AC) para açaí ou (CP) para cuapuaçu:
AC
Por favor, escolha (P)equeno, (M)édio ou (G)rande:
G
Deseja pedir mais alguma coisa?
Digite sim para adicionar mais pedidos ou digite qualquer outra coisa para fechar a conta.
sim
...
Total da sua compra é: R$38,00.
```
# Observações:
- O programa apresenta um cardápio com sabores (Açaí e Cupuaçu) e tamanhos (P, M, G).
- O usuário escolhe o sabor digitando 'AC' ou 'CP' e o tamanho com 'P', 'M' ou 'G'.
- Entradas inválidas são tratadas com mensagens de erro e repetição da pergunta.
- O usuário pode adicionar quantos pedidos quiser, até decidir finalizar.
- O total é acumulado e exibido no final com vírgula no lugar do ponto (formato brasileiro).