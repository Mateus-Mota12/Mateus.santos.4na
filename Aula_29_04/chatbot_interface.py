import streamlit as st
import sympy as sp
import google.generativeai as genai

# Coloque sua chave de API do Gemini aqui
genai.configure(api_key="Sua ChaveAPI")

# Inicializa o modelo Gemini
model = genai.GenerativeModel()

# Tenta resolver expressões matemáticas com sympy
def realizar_calculo(expressao):
    try:
        expr = sp.sympify(expressao)
        resultado = expr.evalf()
        return f"O resultado de `{expressao}` é {resultado}"
    except Exception:
        return None

# Chamada à API do Gemini
def gemini_resposta(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao consultar a IA Gemini: {str(e)}"

# Decide qual resposta usar
def chatbot_resposta(user_input):
    # Tenta realizar um cálculo primeiro
    resultado_calculo = realizar_calculo(user_input)
    if resultado_calculo:
        return resultado_calculo

    # Se não for cálculo, chama a API do Gemini para responder
    return gemini_resposta(user_input)

# Configuração do Streamlit
st.set_page_config(page_title="ChatBot The Rock Anos 90", layout="centered")

# Aplicando o tema personalizado (fundo escuro, cores das mensagens)
st.markdown(
    """
    <style>
        body {
            background-color: #2e2e2e;  /* Cor de fundo escura */
            color: white;
        }
        .stChatMessage[data-testid="stChatMessageContent"] {
            padding: 8px 12px;
            border-radius: 8px;
        }
        .stChatMessage[data-testid="stChatMessageContent"]:nth-child(even) {
            background-color: #1e90ff;  /* Azul para as respostas do chatbot */
            color: white;
        }
        .stChatMessage[data-testid="stChatMessageContent"]:nth-child(odd) {
            background-color: #f0f0f0;  /* Cor neutra para as perguntas do usuário */
            color: black;
        }
        .stTitle {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título da página
st.title("ChatBot The Rock Anos 90")

# Inicializa o histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Olá! Sou o ChatBot The Rock Anos 90. Como posso te ajudar?"}]

# Exibe histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Digite sua pergunta"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    resposta = chatbot_resposta(prompt)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    st.rerun()
