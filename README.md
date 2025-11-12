# Agente‑de‑IA

Uma interface simples de chatbot em Python que integra com a API do ChatGoogleGenerativeAI, permitindo conversas com efeito de digitação no console.

## 🚀 Visão Geral

Este projeto demonstra como construir rapidamente um agente de IA baseado em chat, utilizando:

- Linguagem: Python  
- Biblioteca: `langchain_google_genai` para invocar o modelo da Google  
- Arquivo de configuração (`config.json`) para customização  
- Um loop interativo no console com efeito de digitação para respostas — proporcionando uma melhor experiência de usuário.

Ideal para protótipos, bots de Slack/Discord, ou base para aplicações mais completas.

## 🧩 Estrutura do Projeto

```
Agente‑de‑IA/
│
├── chatbot.py         ← Script principal que executa o loop de chat  
├── config.json        ← Arquivo de configuração (API, parâmetros, etc)  
└── .env               ← Variáveis de ambiente (ex: GOOGLE_API_KEY)  
```

### Principais Componentes

- `chatbot.py`:  
  - Carrega variáveis de ambiente via `python-dotenv`.  
  - Configura o modelo `ChatGoogleGenerativeAI(model='gemini‑2.5‑flash')`.  
  - Carrega `config.json` para parâmetros do chat.  
  - Define função de “efeito de digitação” no console.  
  - Loop principal para leitura de entrada do usuário, chamada ao modelo, e exibição da resposta.

- `config.json`: Arquivo JSON com parâmetros ajustáveis (por exemplo, temperatura, max_tokens, etc).

- `.env`: Aqui você define `GOOGLE_API_KEY=<sua_api_key>` (não subir essa chave para repositório público).

## ✨ Como Usar

1. Clone o repositório:  
   ```bash
   git clone https://github.com/Renanntj/Agente-de-IA.git
   cd Agente-de-IA
   ```

2. Instale as dependências (exemplo):  
   ```bash
   pip install python-dotenv langchain-google-genai
   ```

3. Crie um arquivo `.env` com sua chave de API:  
   ```text
   GOOGLE_API_KEY=seu_token_aqui
   ```

4. Ajuste `config.json` conforme suas necessidades (temperatura, modelo, etc).

5. Execute o chatbot:  
   ```bash
   python chatbot.py
   ```

6. Digite sua mensagem no console. Para sair, digite `SAIR`.

## 🛠️ Personalizações Possíveis

Como professor e empreendedor, aqui estão algumas ideias de evolução:

- Adicionar um sistema de logs para registrar todas as conversas.  
- Integrar com plataformas de chat (Telegram, Discord, Slack, WhatsApp).  
- Melhoria do UI: criar interface web (Flask/Django) ou GUI (Tkinter/PyQt).  
- Implementar memory state avançado: o bot “lembra” contexto entre conversas.  
- Suporte multilíngue ou tradução dinâmica.

## 🧠 Boas Práticas

- Nunca commit sua chave de API no repositório. Use `.gitignore` para `.env`.  
- Use variáveis de ambiente para segredos.  
- Documente bem as configurações no `config.json` para facilitar para outros desenvolvedores.  
- Teste localmente antes de produzir em produção.

## 📄 Licença

Este projeto está licenciado sob a licença MIT — sinta‑se à vontade para usar, modificar e distribuir.
