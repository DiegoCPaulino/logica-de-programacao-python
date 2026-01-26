import streamlit as st

# CONFIGURAÇÃO INICIAL E CREDENCIAIS DE ADMIN
USUARIO_ADMIN = "useradm"
SENHA_ADMIN = "adm123"

# INICIALIZAÇÃO DO SESSION STATE
def inicializar_session_state():
    """Inicializa o session_state para armazenar os dados da aplicação."""
    
    if "instituicoes" not in st.session_state:
        st.session_state.instituicoes = []
    if "cooperativas" not in st.session_state:
        st.session_state.cooperativas = []
    if "profissionais" not in st.session_state:
        st.session_state.profissionais = []
    if "cursos" not in st.session_state:
        st.session_state.cursos = []
        
    if "cursos_concluidos" not in st.session_state:
        st.session_state.cursos_concluidos = [] 
        
    if "cursos_associados" not in st.session_state:
        st.session_state.cursos_associados = []

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_type" not in st.session_state:
        st.session_state.user_type = None
    if "user_info" not in st.session_state:
        st.session_state.user_info = None

# FUNÇÕES DE VALIDAÇÃO E FORMATAÇÃO
def limpar_numeros(texto):
    """Função auxiliar para remover tudo que não for dígito."""
    numeros_limpos = ""
    for char in texto:
        if char.isdigit():
            numeros_limpos += char

    return numeros_limpos

def validar_usuario(user):
    if not (5 <= len(user) <= 15):
        return "Usuário: deve ter entre 5 e 15 caracteres."
    
    letras_min = 0
    numeros = 0
    for char in user:
        if char.islower():
            letras_min += 1
        elif char.isdigit():
            numeros += 1
        else:
            # Se não for minúscula nem dígito, é especial ou maiúscula
            return "Usuário: não pode conter caracteres especiais ou letras maiúsculas."
    
    if letras_min < 3:
        return "Usuário: deve conter pelo menos 3 letras minúsculas."
    if numeros > 6:
        return "Usuário: pode conter no máximo 6 números."
   
    return None

def validar_senha(senha):
    if not (5 <= len(senha) <= 15):
        return "Senha: deve ter entre 5 e 15 caracteres."
    
    tem_letra = False
    tem_numero = False
    tem_especial = False

    especiais = "!@#$%^&*(),.?\":{}|<>"
    
    for char in senha:
        if char.isalpha():
            tem_letra = True
        elif char.isdigit():
            tem_numero = True
        elif char in especiais:
            tem_especial = True
            
    if not tem_letra:
        return "Senha: deve conter pelo menos 1 letra."
    if not tem_numero:
        return "Senha: deve conter pelo menos 1 número."
    if not tem_especial:
        return "Senha: deve conter pelo menos 1 caractere especial."
    
    return None

def validar_string_simples(texto, nome_campo, min_len=1, max_len=50):
    if not (min_len <= len(texto) <= max_len):
        return f"{nome_campo}: deve ter entre {min_len} e {max_len} caracteres."
    
    return None

def validar_descricao(texto, nome_campo, min_len=40, max_len=500):
    if not (min_len <= len(texto) <= max_len):
        return f"{nome_campo}: deve ter entre {min_len} e {max_len} caracteres."
    
    return None

def validar_email(email):
    if "@" not in email or "." not in email:
        return "Email: formato inválido (deve conter @ e .)"
    if email.startswith("@") or email.endswith(".") or email.startswith("."):
        return "Email: formato inválido."
    
    return None

def validar_cnpj(cnpj):
    cnpj_limpo = limpar_numeros(cnpj)
    if len(cnpj_limpo) != 14:
        return "CNPJ: deve conter 14 dígitos."
    primeiro_digito = cnpj_limpo[0]
    todos_iguais = True
    for digito in cnpj_limpo:
        if digito != primeiro_digito:
            todos_iguais = False
            break
    if todos_iguais:
        return "CNPJ: inválido (todos os números são iguais)."
    
    return None

def formatar_cnpj(cnpj):
    cnpj_limpo = limpar_numeros(cnpj)
    if len(cnpj_limpo) == 14:
        return f"{cnpj_limpo[:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:]}"
    
    return cnpj

def validar_cpf(cpf):
    cpf_limpo = limpar_numeros(cpf)
    if len(cpf_limpo) != 11:
        return "CPF: inválido (deve ter 11 dígitos)."
    
    primeiro_digito = cpf_limpo[0]
    todos_iguais = True
    for digito in cpf_limpo:
        if digito != primeiro_digito:
            todos_iguais = False
            break
    if todos_iguais:
        return "CPF: inválido (todos os números são iguais)."
        
    return None

def formatar_cpf(cpf):
    cpf_limpo = limpar_numeros(cpf)
    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    
    return cpf

def validar_data_nascimento(data_str):
    data_limpa = limpar_numeros(data_str)
    if len(data_limpa) != 6:
        return "Data de Nascimento: deve ter 6 dígitos (DDMMAA)."
    
    return None

def validar_data_conclusao(data_str):
    data_limpa = limpar_numeros(data_str)
    if len(data_limpa) != 6:
        return "Data de Conclusão: deve ter 6 dígitos (DDMMAA)."
    
    return None

def formatar_data(data_str):
    data_limpa = limpar_numeros(data_str)
    if len(data_limpa) == 6:
        return f"{data_limpa[0:2]}/{data_limpa[2:4]}/{data_limpa[4:6]}"
    
    return data_str

def validar_horas_curso(horas_str):
    horas_str = horas_str.strip()
    if not horas_str.isdigit():
        return "Horas de Curso: formato inválido (deve ser apenas o número de horas, ex: '40')."
    
    # Tenta converter para número para checar o valor
    try:
        horas_num = int(horas_str)
        if not (1 <= horas_num <= 999):
            return "Horas de Curso: deve ser entre 1 e 999."
    except:
        return "Horas de Curso: número inválido."
    
    return None

def formatar_horas_curso(horas_str):
    horas_str = horas_str.strip()
    if horas_str.isdigit():
        return f"{int(horas_str)}h"
    
    return horas_str

# FUNÇÕES DE AUTENTICAÇÃO
def logar_usuario(user, senha, user_type):
    """Tenta logar o usuário e atualiza o session_state."""
    
    if user == USUARIO_ADMIN and senha == SENHA_ADMIN:
        st.session_state.logged_in = True
        st.session_state.user_type = "admin"
        st.session_state.user_info = {"usuario": "admin", "nome": "Administrador"}
        st.rerun()
        return

    lista_usuarios = []
    if user_type == "Cooperativa":
        lista_usuarios = st.session_state.cooperativas
    elif user_type == "Profissional":
        lista_usuarios = st.session_state.profissionais
    elif user_type == "Instituição de Ensino":
        lista_usuarios = st.session_state.instituicoes
    else:
        st.error("Tipo de usuário inválido.")
        return

    for usuario_data in lista_usuarios:
        if usuario_data.get("usuario") == user and usuario_data.get("senha") == senha:
            st.session_state.logged_in = True
            st.session_state.user_type = user_type.lower().replace(" ", "_")
            st.session_state.user_info = usuario_data
            st.rerun()
            return
    
    st.error("Usuário ou senha incorretos.")

def deslogar_usuario():
    """Desloga o usuário e reseta o session_state."""
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.user_info = None
    st.rerun()

# TELAS DE CADASTRO
def cadastro_cooperativa():
    st.header("Cadastro de Cooperativa")
    
    cursos_disponiveis = []
    for c in st.session_state.cursos:
        cursos_disponiveis.append(c["nome_curso"])
        
    if not cursos_disponiveis:
        st.info("Nenhum curso cadastrado no sistema ainda. Você pode associar cursos mais tarde.")

    with st.form("form_cooperativa"):
        st.subheader("Credenciais")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        
        st.subheader("Dados da Cooperativa")
        nome = st.text_input("Nome da Cooperativa")
        area_atuacao = st.text_input("Área de Atuação")
        cnpj = st.text_input("CNPJ (somente números)")
        email = st.text_input("Email para Contato")
        descricao = st.text_area("Descrição da Cooperativa")
        
        st.subheader("Cursos Requisitados")
        cursos_selecionados = st.multiselect(
            "Selecione os cursos que os profissionais deverão ter:",
            cursos_disponiveis
        )
        
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            erros = []
            
            erro_v = validar_usuario(usuario)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_senha(senha)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_string_simples(nome, "Nome da Cooperativa")
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_string_simples(area_atuacao, "Área de Atuação")
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_cnpj(cnpj)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_email(email)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_descricao(descricao, "Descrição")
            if erro_v: erros.append(erro_v)
            
            
            cnpj_formatado = formatar_cnpj(cnpj)
            
            cnpj_existe = False
            for c in st.session_state.cooperativas:
                if c["cnpj"] == cnpj_formatado:
                    cnpj_existe = True
                    break
            if cnpj_existe:
                erros.append("CNPJ já cadastrado.")
            
            usuario_existe = False
            for c in st.session_state.cooperativas:
                if c["usuario"] == usuario:
                    usuario_existe = True
                    break
            if usuario_existe:
                erros.append("Nome de usuário já cadastrado.")

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                nova_cooperativa = {
                    "usuario": usuario,
                    "senha": senha,
                    "nome": nome,
                    "area_atuacao": area_atuacao,
                    "cnpj": cnpj_formatado,
                    "email": email,
                    "descricao": descricao,
                }
                st.session_state.cooperativas.append(nova_cooperativa)
                
                for curso_nome in cursos_selecionados:
                    st.session_state.cursos_associados.append({
                        "cnpj_cooperativa": cnpj_formatado,
                        "nome_curso": curso_nome
                    })
                
                st.success("Cooperativa cadastrada com sucesso! Faça o login.")

def cadastro_profissional():
    st.header("Cadastro de Profissional")

    with st.form("form_profissional"):
        st.subheader("Credenciais")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        
        st.subheader("Dados Pessoais")
        nome_completo = st.text_input("Nome Completo")
        cpf = st.text_input("CPF (somente números)")
        data_nascimento = st.text_input("Data de Nascimento (DDMMAA)")
        
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            erros = []
            
            erro_v = validar_usuario(usuario)
            if erro_v: erros.append(erro_v)

            erro_v = validar_senha(senha)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_string_simples(nome_completo, "Nome Completo")
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_cpf(cpf)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_data_nascimento(data_nascimento)
            if erro_v: erros.append(erro_v)

            cpf_formatado = formatar_cpf(cpf)
            
            cpf_existe = False
            for p in st.session_state.profissionais:
                if p["cpf"] == cpf_formatado:
                    cpf_existe = True
                    break
            if cpf_existe:
                erros.append("CPF já cadastrado.")
            
            usuario_existe = False
            for p in st.session_state.profissionais:
                if p["usuario"] == usuario:
                    usuario_existe = True
                    break
            if usuario_existe:
                erros.append("Nome de usuário já cadastrado.")

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                novo_profissional = {
                    "usuario": usuario,
                    "senha": senha,
                    "nome": nome_completo,
                    "cpf": cpf_formatado,
                    "data_nascimento": formatar_data(data_nascimento),
                }
                st.session_state.profissionais.append(novo_profissional)
                st.success("Profissional cadastrado com sucesso! Faça o login.")

def cadastro_instituicao():
    st.header("Cadastro de Instituição de Ensino")

    with st.form("form_instituicao"):
        st.subheader("Credenciais")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        
        st.subheader("Dados da Instituição")
        nome = st.text_input("Nome da Instituição")
        cnpj = st.text_input("CNPJ (somente números)")
        email = st.text_input("Email para Contato")
        
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            erros = []
            
            erro_v = validar_usuario(usuario)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_senha(senha)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_string_simples(nome, "Nome da Instituição")
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_cnpj(cnpj)
            if erro_v: erros.append(erro_v)
            
            erro_v = validar_email(email)
            if erro_v: erros.append(erro_v)
            
            cnpj_formatado = formatar_cnpj(cnpj)
            
            cnpj_existe = False
            for i in st.session_state.instituicoes:
                if i["cnpj"] == cnpj_formatado:
                    cnpj_existe = True
                    break
            if cnpj_existe:
                erros.append("CNPJ já cadastrado.")

            usuario_existe = False
            for i in st.session_state.instituicoes:
                if i["usuario"] == usuario:
                    usuario_existe = True
                    break
            if usuario_existe:
                erros.append("Nome de usuário já cadastrado.")

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                nova_instituicao = {
                    "usuario": usuario,
                    "senha": senha,
                    "nome": nome,
                    "cnpj": cnpj_formatado,
                    "email": email,
                }
                st.session_state.instituicoes.append(nova_instituicao)
                st.success("Instituição cadastrada com sucesso! Faça o login.")

# MENUS PRINCIPAIS
def mostrar_menu_cooperativa():
    st.sidebar.title(f"Bem-vindo(a), {st.session_state.user_info['nome']}")
    menu_options = [
        "Meu Perfil",
        "Buscar Profissionais",
        "Associar/Alterar Cursos",
        "Alterar Informações"
    ]
    menu = st.sidebar.radio("Menu Cooperativa", menu_options)
    st.sidebar.button("Logout", on_click=deslogar_usuario)
    
    if menu == "Meu Perfil":
        st.header("Perfil da Cooperativa")
        info = st.session_state.user_info
        st.write(f"**Nome:** {info['nome']}")
        st.write(f"**CNPJ:** {info['cnpj']}")
        st.write(f"**Email:** {info['email']}")
        st.write(f"**Área de Atuação:** {info['area_atuacao']}")
        st.write(f"**Descrição:** {info['descricao']}")
        
        st.subheader("Cursos Associados Atualmente")
        meu_cnpj = info['cnpj']
        
        cursos_associados = []
        for c in st.session_state.cursos_associados:
            if c['cnpj_cooperativa'] == meu_cnpj:
                cursos_associados.append(c['nome_curso'])
        
        if cursos_associados:
            for curso in cursos_associados:
                st.write(f"- {curso}")
        else:
            st.info("Nenhum curso associado no momento.")

    elif menu == "Buscar Profissionais":
        st.header("Buscar Profissionais por Curso")
        
        cursos_disponiveis = []
        for c in st.session_state.cursos:
            cursos_disponiveis.append(c["nome_curso"])

        if not cursos_disponiveis:
            st.warning("Nenhum curso cadastrado no sistema para busca.")
            return

        curso_selecionado = st.selectbox("Selecione o curso:", [""] + cursos_disponiveis)

        if curso_selecionado:
            cpfs_profissionais = []
            for c in st.session_state.cursos_concluidos:
                if c['nome_curso'] == curso_selecionado:
                    cpfs_profissionais.append(c['cpf_profissional'])
            
            if not cpfs_profissionais:
                st.info(f"Nenhum profissional concluiu o curso '{curso_selecionado}'.")
                return

            st.subheader(f"Profissionais que concluíram '{curso_selecionado}':")
            for prof in st.session_state.profissionais:
                if prof['cpf'] in cpfs_profissionais:
                    st.write(f"**Nome:** {prof['nome']} | **CPF:** {prof['cpf']}")

    elif menu == "Associar/Alterar Cursos":
        st.header("Associar/Alterar Cursos Requisitados")
        
        cursos_disponiveis = []
        for c in st.session_state.cursos:
            cursos_disponiveis.append(c["nome_curso"])
            
        if not cursos_disponiveis:
            st.warning("Nenhum curso disponível no sistema para associar.")
            return
            
        meu_cnpj = st.session_state.user_info['cnpj']
        
        cursos_atuais = []
        for c in st.session_state.cursos_associados:
            if c['cnpj_cooperativa'] == meu_cnpj:
                cursos_atuais.append(c['nome_curso'])
        
        cursos_selecionados = st.multiselect(
            "Selecione os cursos que sua cooperativa exige:",
            cursos_disponiveis,
            default=cursos_atuais
        )

        if st.button("Salvar Alterações de Cursos"):
            nova_lista_associados = []
            for c in st.session_state.cursos_associados:
                if c['cnpj_cooperativa'] != meu_cnpj:
                    nova_lista_associados.append(c)
            
            for curso_nome in cursos_selecionados:
                nova_lista_associados.append({
                    "cnpj_cooperativa": meu_cnpj,
                    "nome_curso": curso_nome
                })
            
            st.session_state.cursos_associados = nova_lista_associados
            st.success("Cursos associados atualizados com sucesso!")
            st.rerun()

    elif menu == "Alterar Informações":
        st.header("Alterar Informações Cadastrais")
        
        info = st.session_state.user_info
        
        with st.form("form_alterar_cooperativa"):
            st.subheader("Credenciais (deixe em branco para não alterar)")
            senha = st.text_input("Nova Senha", type="password")
            
            st.subheader("Dados da Cooperativa")
            nome = st.text_input("Nome da Cooperativa", value=info['nome'])
            area_atuacao = st.text_input("Área de Atuação", value=info['area_atuacao'])
            cnpj = st.text_input("CNPJ", value=info['cnpj'], disabled=True)
            email = st.text_input("Email para Contato", value=info['email'])
            descricao = st.text_area("Descrição da Cooperativa", value=info['descricao'])
            
            submitted = st.form_submit_button("Salvar Alterações")

            if submitted:
                erros = []
                
                if senha: 
                    erro_v = validar_senha(senha)
                    if erro_v: erros.append(erro_v)
                
                erro_v = validar_string_simples(nome, "Nome da Cooperativa")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_string_simples(area_atuacao, "Área de Atuação")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_email(email)
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_descricao(descricao, "Descrição")
                if erro_v: erros.append(erro_v)

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    for i, coop in enumerate(st.session_state.cooperativas):
                        if coop['cnpj'] == info['cnpj']:
                            if senha:
                                st.session_state.cooperativas[i]['senha'] = senha
                            st.session_state.cooperativas[i]['nome'] = nome
                            st.session_state.cooperativas[i]['area_atuacao'] = area_atuacao
                            st.session_state.cooperativas[i]['email'] = email
                            st.session_state.cooperativas[i]['descricao'] = descricao
                            
                            st.session_state.user_info = st.session_state.cooperativas[i]
                            break
                    
                    st.success("Informações atualizadas com sucesso!")
                    st.rerun()

def mostrar_menu_profissional():
    st.sidebar.title(f"Bem-vindo(a), {st.session_state.user_info['nome']}")
    menu_options = [
        "Meu Perfil",
        "Cadastrar Conclusão de Curso",
        "Consultar Cooperativas",
        "Consultar Cursos Disponíveis",
        "Alterar Informações"
    ]
    menu = st.sidebar.radio("Menu Profissional", menu_options)
    st.sidebar.button("Logout", on_click=deslogar_usuario)
    
    info = st.session_state.user_info
    meu_cpf = info['cpf']

    if menu == "Meu Perfil":
        st.header("Perfil do Profissional")
        st.write(f"**Nome:** {info['nome']}")
        st.write(f"**CPF:** {info['cpf']}")
        st.write(f"**Data de Nascimento:** {info['data_nascimento']}")
        
        st.subheader("Meus Cursos Concluídos")
        
        meus_cursos = []
        for c in st.session_state.cursos_concluidos:
            if c['cpf_profissional'] == meu_cpf:
                meus_cursos.append(c)
                
        if meus_cursos:
            for curso in meus_cursos:
                st.write(f"- **{curso['nome_curso']}** (Concluído em: {curso['data_conclusao']})")
        else:
            st.info("Você ainda não cadastrou nenhum curso concluído.")

    elif menu == "Cadastrar Conclusão de Curso":
        st.header("Cadastrar Conclusão de Curso")
        
        cursos_disponiveis = []
        for c in st.session_state.cursos:
            cursos_disponiveis.append(c["nome_curso"])
            
        if not cursos_disponiveis:
            st.warning("Nenhum curso disponível no sistema para cadastrar.")
            return

        with st.form("form_conclusao_curso"):
            curso_selecionado = st.selectbox("Selecione o curso concluído:", cursos_disponiveis)
            data_conclusao = st.text_input("Data da Conclusão (DDMMAA)")
            submitted = st.form_submit_button("Cadastrar Conclusão")

            if submitted:
                erros = []
                
                erro_v = validar_data_conclusao(data_conclusao)
                if erro_v:
                    erros.append(erro_v)
                
                ja_cadastrado = False
                for c in st.session_state.cursos_concluidos:
                    if c['cpf_profissional'] == meu_cpf and c['nome_curso'] == curso_selecionado:
                        ja_cadastrado = True
                        break
                if ja_cadastrado:
                    erros.append("Você já cadastrou a conclusão para este curso.")
                
                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    st.session_state.cursos_concluidos.append({
                        "cpf_profissional": meu_cpf,
                        "nome_curso": curso_selecionado,
                        "data_conclusao": formatar_data(data_conclusao)
                    })
                    st.success(f"Curso '{curso_selecionado}' cadastrado com sucesso!")

    elif menu == "Consultar Cooperativas":
        st.header("Cooperativas Cadastradas")
        
        if not st.session_state.cooperativas:
            st.info("Nenhuma cooperativa cadastrada no sistema.")
            return

        for coop in st.session_state.cooperativas:
            with st.expander(f"{coop['nome']} - {coop['area_atuacao']}"):
                st.write(f"**Email:** {coop['email']}")
                st.write(f"**Descrição:** {coop['descricao']}")
                
                # Substituindo List Comprehension por loop For
                cursos_req = []
                for c in st.session_state.cursos_associados:
                    if c['cnpj_cooperativa'] == coop['cnpj']:
                        cursos_req.append(c['nome_curso'])
                
                if cursos_req:
                    st.write("**Cursos Requeridos:**")
                    for curso in cursos_req:
                        st.write(f"- {curso}")
                else:
                    st.write("**Cursos Requeridos:** Nenhum especificado.")

    elif menu == "Consultar Cursos Disponíveis":
        st.header("Cursos Disponíveis no Sistema")
        
        if not st.session_state.cursos:
            st.info("Nenhum curso cadastrado no sistema.")
            return
        
        for curso in st.session_state.cursos:
            with st.expander(f"{curso['nome_curso']} ({curso['horas']})"):
                inst_nome = "Não encontrada"
                # Loop para achar o nome da instituição pelo CNPJ
                for inst in st.session_state.instituicoes:
                    if inst['cnpj'] == curso['cnpj_instituicao']:
                        inst_nome = inst['nome']
                        break
                        
                st.write(f"**Instituição:** {inst_nome}")
                st.write(f"**Professor:** {curso['professor']}")
                st.write(f"**Descrição:** {curso['descricao']}")

    elif menu == "Alterar Informações":
        st.header("Alterar Informações Cadastrais")
        
        with st.form("form_alterar_profissional"):
            st.subheader("Credenciais (deixe em branco para não alterar)")
            senha = st.text_input("Nova Senha", type="password")
            
            st.subheader("Dados Pessoais")
            nome_completo = st.text_input("Nome Completo", value=info['nome'])
            cpf = st.text_input("CPF", value=info['cpf'], disabled=True)
            # Usa a função 'limpar_numeros' para preencher o campo
            data_nasc_limpa = limpar_numeros(info['data_nascimento'])
            data_nascimento = st.text_input("Data de Nascimento (DDMMAA)", value=data_nasc_limpa)

            submitted = st.form_submit_button("Salvar Alterações")

            if submitted:
                erros = []
                
                # Substituindo operador Walrus (:=)
                if senha:
                    erro_v = validar_senha(senha)
                    if erro_v: erros.append(erro_v)
                
                erro_v = validar_string_simples(nome_completo, "Nome Completo")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_data_nascimento(data_nascimento)
                if erro_v: erros.append(erro_v)

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    # Loop para encontrar e atualizar o profissional
                    for i, prof in enumerate(st.session_state.profissionais):
                        if prof['cpf'] == info['cpf']:
                            if senha:
                                st.session_state.profissionais[i]['senha'] = senha
                            st.session_state.profissionais[i]['nome'] = nome_completo
                            st.session_state.profissionais[i]['data_nascimento'] = formatar_data(data_nascimento)
                            
                            st.session_state.user_info = st.session_state.profissionais[i]
                            break
                    
                    st.success("Informações atualizadas com sucesso!")
                    st.rerun()

def mostrar_menu_instituicao():
    st.sidebar.title(f"Bem-vindo(a), {st.session_state.user_info['nome']}")
    menu_options = [
        "Meu Perfil",
        "Cadastrar Novo Curso",
        "Listar Meus Cursos",
        "Consultar Cooperativas (por Cursos)",
        "Consultar Profissionais (por Cursos)",
        "Alterar Informações"
    ]
    menu = st.sidebar.radio("Menu Instituição", menu_options)
    st.sidebar.button("Logout", on_click=deslogar_usuario)
    
    info = st.session_state.user_info
    meu_cnpj = info['cnpj']

    if menu == "Meu Perfil":
        st.header("Perfil da Instituição")
        st.write(f"**Nome:** {info['nome']}")
        st.write(f"**CNPJ:** {info['cnpj']}")
        st.write(f"**Email:** {info['email']}")

    elif menu == "Cadastrar Novo Curso":
        st.header("Cadastrar Novo Curso")
        
        with st.form("form_novo_curso"):
            nome_curso = st.text_input("Nome do Curso")
            professor = st.text_input("Professor do Curso")
            horas_curso = st.text_input("Horas de Curso (ex: '40')")
            descricao = st.text_area("Descrição do Curso")
            
            submitted = st.form_submit_button("Cadastrar Curso")
            
            if submitted:
                erros = []
                
                erro_v = validar_string_simples(nome_curso, "Nome do Curso")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_string_simples(professor, "Professor")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_horas_curso(horas_curso)
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_descricao(descricao, "Descrição do Curso")
                if erro_v: erros.append(erro_v)
                
                curso_existe = False
                for c in st.session_state.cursos:
                    if c['nome_curso'].lower() == nome_curso.lower():
                        curso_existe = True
                        break
                if curso_existe:
                    erros.append("Já existe um curso com este nome no sistema.")

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    novo_curso = {
                        "cnpj_instituicao": meu_cnpj,
                        "nome_curso": nome_curso,
                        "professor": professor,
                        "horas": formatar_horas_curso(horas_curso),
                        "descricao": descricao,
                    }
                    st.session_state.cursos.append(novo_curso)
                    st.success(f"Curso '{nome_curso}' cadastrado com sucesso!")

    elif menu == "Listar Meus Cursos":
        st.header("Meus Cursos Cadastrados")
        
        meus_cursos = []
        for c in st.session_state.cursos:
            if c['cnpj_instituicao'] == meu_cnpj:
                meus_cursos.append(c)
        
        if not meus_cursos:
            st.info("Você ainda não cadastrou nenhum curso.")
            return

        for curso in meus_cursos:
            with st.expander(f"{curso['nome_curso']} ({curso['horas']})"):
                st.write(f"**Professor:** {curso['professor']}")
                st.write(f"**Descrição:** {curso['descricao']}")

    elif menu == "Consultar Cooperativas (por Cursos)":
        st.header("Cooperativas que utilizam seus Cursos")
        
        meus_cursos_nomes = []
        for c in st.session_state.cursos:
            if c['cnpj_instituicao'] == meu_cnpj:
                meus_cursos_nomes.append(c['nome_curso'])
        
        if not meus_cursos_nomes:
            st.info("Você não tem cursos cadastrados para consultar.")
            return

        cooperativas_encontradas = {} 
        
        for assoc in st.session_state.cursos_associados:
            if assoc['nome_curso'] in meus_cursos_nomes:
                cnpj_coop = assoc['cnpj_cooperativa']
                if cnpj_coop not in cooperativas_encontradas:
                    cooperativas_encontradas[cnpj_coop] = []
                cooperativas_encontradas[cnpj_coop].append(assoc['nome_curso'])
        
        if not cooperativas_encontradas:
            st.info("Nenhuma cooperativa associou seus cursos ainda.")
            return
            
        for cnpj_coop, cursos_usados in cooperativas_encontradas.items():
            nome_coop = "Cooperativa não encontrada"
            for coop in st.session_state.cooperativas:
                if coop['cnpj'] == cnpj_coop:
                    nome_coop = coop['nome']
                    break
            
            st.subheader(f"{nome_coop} (CNPJ: {cnpj_coop})")
            st.write("Utiliza os seguintes cursos seus:")
            for curso_nome in cursos_usados:
                st.write(f"- {curso_nome}")

    elif menu == "Consultar Profissionais (por Cursos)":
        st.header("Profissionais que concluíram seus Cursos")

        meus_cursos_nomes = []
        for c in st.session_state.cursos:
            if c['cnpj_instituicao'] == meu_cnpj:
                meus_cursos_nomes.append(c['nome_curso'])
        
        if not meus_cursos_nomes:
            st.info("Você não tem cursos cadastrados para consultar.")
            return

        profissionais_encontrados = {}

        for conclusao in st.session_state.cursos_concluidos:
            if conclusao['nome_curso'] in meus_cursos_nomes:
                cpf_prof = conclusao['cpf_profissional']
                if cpf_prof not in profissionais_encontrados:
                    profissionais_encontrados[cpf_prof] = []
                profissionais_encontrados[cpf_prof].append(conclusao['nome_curso'])
        
        if not profissionais_encontrados:
            st.info("Nenhum profissional concluiu seus cursos ainda.")
            return
            
        for cpf_prof, cursos_concluidos in profissionais_encontrados.items():
            nome_prof = "Profissional não encontrado"
            for prof in st.session_state.profissionais:
                if prof['cpf'] == cpf_prof:
                    nome_prof = prof['nome']
                    break
            
            st.subheader(f"{nome_prof} (CPF: {cpf_prof})")
            st.write("Concluiu os seguintes cursos seus:")
            for curso_nome in cursos_concluidos:
                st.write(f"- {curso_nome}")
                
    elif menu == "Alterar Informações":
        st.header("Alterar Informações Cadastrais")
        
        with st.form("form_alterar_instituicao"):
            st.subheader("Credenciais (deixe em branco para não alterar)")
            senha = st.text_input("Nova Senha", type="password")
            
            st.subheader("Dados da Instituição")
            nome = st.text_input("Nome da Instituição", value=info['nome'])
            cnpj = st.text_input("CNPJ", value=info['cnpj'], disabled=True)
            email = st.text_input("Email para Contato", value=info['email'])
            
            submitted = st.form_submit_button("Salvar Alterações")

            if submitted:
                erros = []
                
                if senha:
                    erro_v = validar_senha(senha)
                    if erro_v: erros.append(erro_v)

                erro_v = validar_string_simples(nome, "Nome da Instituição")
                if erro_v: erros.append(erro_v)
                
                erro_v = validar_email(email)
                if erro_v: erros.append(erro_v)

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    for i, inst in enumerate(st.session_state.instituicoes):
                        if inst['cnpj'] == info['cnpj']:
                            if senha:
                                st.session_state.instituicoes[i]['senha'] = senha
                            st.session_state.instituicoes[i]['nome'] = nome
                            st.session_state.instituicoes[i]['email'] = email
                            
                            st.session_state.user_info = st.session_state.instituicoes[i]
                            break
                    
                    st.success("Informações atualizadas com sucesso!")
                    st.rerun()

def mostrar_menu_admin():
    st.sidebar.title("Painel do Administrador")
    menu_options = [
        "Listar Cooperativas",
        "Listar Profissionais",
        "Listar Instituições",
        "Listar Cursos"
    ]
    menu = st.sidebar.radio("Menu Admin", menu_options)
    st.sidebar.button("Logout", on_click=deslogar_usuario)
    
    if menu == "Listar Cooperativas":
        st.header("Cooperativas Cadastradas")
        st.dataframe(st.session_state.cooperativas)
        
    elif menu == "Listar Profissionais":
        st.header("Profissionais Cadastrados")
        st.dataframe(st.session_state.profissionais)
        
    elif menu == "Listar Instituições":
        st.header("Instituições Cadastradas")
        st.dataframe(st.session_state.instituicoes)
        
    elif menu == "Listar Cursos":
        st.header("Cursos Cadastrados")
        st.dataframe(st.session_state.cursos)
        
        st.header("Cursos Associados (Cooperativas)")
        st.dataframe(st.session_state.cursos_associados)
        
        st.header("Cursos Concluídos (Profissionais)")
        st.dataframe(st.session_state.cursos_concluidos)

# FLUXO PRINCIPAL DA APLICAÇÃO
def main():
    """Função principal que controla o fluxo da aplicação."""
    
    inicializar_session_state()

    if not st.session_state.logged_in:
        st.title("Sistema de Gestão de Cursos e Cooperativas")
        
        tab_login, tab_coop, tab_prof, tab_inst = st.tabs([
            "Login", 
            "Cadastro Cooperativa", 
            "Cadastro Profissional", 
            "Cadastro Instituição"
        ])

        with tab_login:
            st.header("Login")
            user_type = st.selectbox(
                "Eu sou:",
                ["Cooperativa", "Profissional", "Instituição de Ensino"]
            )
            user = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            if st.button("Logar"):
                logar_usuario(user, senha, user_type)
        
        with tab_coop:
            cadastro_cooperativa()
            
        with tab_prof:
            cadastro_profissional()
            
        with tab_inst:
            cadastro_instituicao()

    else:
        if st.session_state.user_type == "cooperativa":
            mostrar_menu_cooperativa()
        elif st.session_state.user_type == "profissional":
            mostrar_menu_profissional()
        elif st.session_state.user_type == "instituição_de_ensino":
            mostrar_menu_instituicao()
        elif st.session_state.user_type == "admin":
            mostrar_menu_admin()
        else:
            st.error("Tipo de usuário desconhecido. Fazendo logout.")
            deslogar_usuario()

# PONTO DE ENTRADA
if __name__ == "__main__":
    main()