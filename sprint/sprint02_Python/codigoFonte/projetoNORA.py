import streamlit as st
import re  # Import necessário para regex

# Listas de dados na sessão
if "dentistas" not in st.session_state:
    st.session_state.dentistas = []
if "pacientes" not in st.session_state:
    st.session_state.pacientes = []

# Credenciais para o administrador do sistema
usuarioAdmin = "useradm"
senhaAdmin = "adm123"

# Funções utilitárias
def gerarUsuario(nome):
    primeiroNome = nome.split()[0].lower()
    numero = str(len(st.session_state.dentistas) + 1)
    return primeiroNome + numero
def gerarSenha(nome, cro):
    primeiroNome = nome.split()[0].lower()
    id_dentista = len(st.session_state.dentistas) + 1
    numeros_cro = ''.join(re.findall(r'\d', cro))[:3]
    return f"{primeiroNome}{id_dentista}{numeros_cro}"

# Funções de Validação (Regex)
def validar_nome(nome):
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]{1,}", nome.strip()))
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, peso):
        soma = sum(int(a) * b for a, b in zip(cpf, peso))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dig1 = calc_digito(cpf[:9], range(10, 1, -1))
    dig2 = calc_digito(cpf[:10], range(11, 1, -1))
    return cpf[-2:] == dig1 + dig2
def validar_telefone(telefone):
    return bool(re.fullmatch(r"\d{8,15}", telefone.strip()))
def validar_email(email):
    return bool(re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$", email.strip()))
def validar_cro(cro):
    cro = cro.strip().upper()
    return bool(re.fullmatch(r"^CRO[A-Z]{2}\d{1,6}[A-Z]{0,3}$", cro))
def validar_especialidade(especialidade):
    especialidade = especialidade.strip()
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s\-]{5,}", especialidade))

# Cadastros
def cadastro_paciente():
    st.header("🧍‍♂️ Cadastro de Paciente")

    with st.form("form_paciente"):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF (somente números)")
        telefone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        confirmar = st.form_submit_button("Cadastrar Paciente")

        if confirmar:
            nome, cpf, telefone, email = nome.strip(), cpf.strip(), telefone.strip(), email.strip()
            erros = []
            if not validar_nome(nome):
                erros.append("Nome inválido. Use apenas letras.")
            if not validar_cpf(cpf):
                erros.append("CPF inválido. Verifique os dígitos informados.")
            if not validar_telefone(telefone):
                erros.append("Telefone inválido. Deve conter entre 8 e 15 números.")
            if not validar_email(email):
                erros.append("E-mail inválido. Informe um e-mail válido (ex: nome@dominio.com).")

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                paciente = {
                    "nomeCompleto": nome,
                    "cpf": cpf,
                    "telefone": telefone,
                    "email": email,
                }
                st.session_state.pacientes.append(paciente)
                st.success(f"✅ Paciente {nome} cadastrado com sucesso!")
def cadastro_dentista():
    st.header("🦷 Cadastro de Dentista Voluntário")

    with st.form("form_dentista"):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF (somente números)")
        cro = st.text_input("CRO")
        telefone = st.text_input("Telefone (somente números)")
        email = st.text_input("E-mail")
        especialidade = st.text_input("Especialidade")
        confirmar = st.form_submit_button("Cadastrar Dentista")

        if confirmar:
            # Normalização
            nome, cpf, cro, telefone, email, especialidade = (
                nome.strip(),
                cpf.strip(),
                cro.strip().upper(),
                telefone.strip(),
                email.strip(),
                especialidade.strip(),
            )

            erros = []
            if not validar_nome(nome):
                erros.append("Nome inválido. Use apenas letras.")
            if not validar_cpf(cpf):
                erros.append("CPF inválido. Verifique os dígitos informados.")
            if not validar_cro(cro):
                erros.append("CRO inválido. Use o formato: CROUF12345 ou CROUF12345CD.")
            if not validar_telefone(telefone):
                erros.append("Telefone inválido. Deve conter entre 8 e 15 números.")
            if not validar_email(email):
                erros.append("E-mail inválido.")
            if not validar_especialidade(especialidade):
                erros.append("Especialidade inválida.")

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                usuario = gerarUsuario(nome)
                senha = gerarSenha(nome, cro)
                dentista = {
                    "nomeCompleto": nome,
                    "cpf": cpf,
                    "numeroCro": cro,
                    "telefone": telefone,
                    "email": email,
                    "especialidade": especialidade,
                    "usuario": usuario,
                    "senha": senha,
                }
                st.session_state.dentistas.append(dentista)
                st.success(f"✅ Dentista {nome} cadastrado com sucesso!")
                st.info(f"👤 Usuário: `{usuario}` | 🔑 Senha: `{senha}`")

# Listagens
def listar_dentistas():
    st.header("📋 Dentistas Cadastrados (Acesso Restrito)")
    user = st.text_input("Usuário admin")
    senha = st.text_input("Senha admin", type="password")

    if st.button("Entrar"):
        if user == usuarioAdmin and senha == senhaAdmin:
            if st.session_state.dentistas:
                st.subheader("Dentistas Registrados:")
                for d in st.session_state.dentistas:
                    st.write(f"**{d['nomeCompleto']}** — CRO: {d['numeroCro']} | CPF: {d['cpf']}")
            else:
                st.warning("Nenhum dentista cadastrado ainda.")
        else:
            st.error("Acesso negado. Usuário ou senha incorretos.")
def listar_pacientes():
    st.header("📋 Pacientes Cadastrados (Acesso Restrito)")
    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if user == usuarioAdmin and senha == senhaAdmin:
            if st.session_state.pacientes:
                st.subheader("Pacientes Registrados:")
                for p in st.session_state.pacientes:
                    st.write(f"**{p['nomeCompleto']}** — CPF: {p['cpf']}")
            else:
                st.warning("Nenhum paciente cadastrado.")
        else:
            for d in st.session_state.dentistas:
                if d["usuario"] == user and d["senha"] == senha:
                    st.success(f"Bem-vindo(a), Dr(a). {d['nomeCompleto']}!")
                    if st.session_state.pacientes:
                        for p in st.session_state.pacientes:
                            st.write(f"**{p['nomeCompleto']}** — CPF: {p['cpf']}")
                    else:
                        st.warning("Nenhum paciente cadastrado.")
                    return
            st.error("Acesso negado. Credenciais inválidas.")

# Estrutura de Navegação
st.title("🦷 Sistema de Cadastro TdB")
menu = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Início",
        "🦷 Cadastrar Dentista",
        "🧍 Cadastrar Paciente",
        "📋 Ver Dentistas (Admin)",
        "📋 Ver Pacientes (Restrito)",
    ],
)
if menu == "🏠 Início":
    st.markdown("""
        ### Bem-vindo ao Sistema TdB
        Selecione uma opção no menu lateral para navegar:
        - 🦷 **Dentistas voluntários** podem se cadastrar.  
        - 🧍 **Pacientes** podem registrar seus dados.  
        - 📋 **Administrador** pode visualizar os cadastros.
    """)
elif menu == "🦷 Cadastrar Dentista":
    cadastro_dentista()
elif menu == "🧍 Cadastrar Paciente":
    cadastro_paciente()
elif menu == "📋 Ver Dentistas (Admin)":
    listar_dentistas()
elif menu == "📋 Ver Pacientes (Restrito)":
    listar_pacientes()
