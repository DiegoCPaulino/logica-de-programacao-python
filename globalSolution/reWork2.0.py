import streamlit as st
import time

# Configurações iniciais da página do Streamlit
# Layout "wide" aproveita melhor a largura do monitor
st.set_page_config(page_title="ReWork Circular - Demo", layout="wide")

# --- 1. FUNÇÕES ÚTEIS (AUXILIARES) ---

def limpar_numeros(texto):
    """
    Remove caracteres especiais (pontos, traços, etc) e deixa apenas números.
    Útil para limpar CPF e CNPJ antes de salvar ou comparar.
    """
    apenas_numeros = ""
    for char in str(texto):
        if char.isdigit():
            apenas_numeros += char
    return apenas_numeros

def formatar_cpf(cpf):
    # Formata o CPF para exibição no padrão 000.000.000-00
    # Usa fatiamento de string (slicing) para pegar as partes do número
    numeros = limpar_numeros(cpf)
    if len(numeros) == 11:
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
    return cpf

def formatar_cnpj(cnpj):
    # Formata o CNPJ para exibição no padrão 00.000.000/0000-00
    numeros = limpar_numeros(cnpj)
    if len(numeros) == 14:
        return f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
    return cnpj

def limpar_aviso():
    """
    Função chamada automaticamente quando o usuário troca de aba.
    Serve para limpar mensagens de sucesso/erro antigas da tela.
    """
    if "aviso_sucesso" in st.session_state:
        st.session_state.aviso_sucesso = None

# --- 2. DADOS INICIAIS (SIMULAÇÃO DE BANCO DE DADOS) ---

def inicializar_dados_demo():
    """
    Como não estamos usando um banco de dados real (SQL), 
    criamos listas de dicionários no session_state para armazenar tudo na memória.
    """
    
    # Verifica se os dados já existem para não recarregar/zerar a cada atualização de tela
    if "dados_carregados" not in st.session_state:
        
        # --- DADOS DAS INSTITUIÇÕES DE ENSINO ---
        st.session_state.instituicoes = [
            {
                "id": 1,
                "nome": "Instituto Terra Viva",
                "cnpj": "11221144000100",
                "email": "contato@terraviva.edu.br",
                "cursos": [
                    {"nome_curso": "GreenOps Básico", "horas": "20h", "professor": "Dra. Ana Terra", "descricao": "Introdução a operações verdes."},
                    {"nome_curso": "Gestão de Resíduos Urbanos", "horas": "25h", "professor": "Msc. Carlos Urbano", "descricao": "Gestão técnica de resíduos na cidade."},
                    {"nome_curso": "Operações Circulares", "horas": "30h", "professor": "Prof. Julia Ciclo", "descricao": "Como aplicar circularidade na indústria."}
                ]
            },
            {
                "id": 2,
                "nome": "Centro ESG Futuro",
                "cnpj": "19449933000100",
                "email": "cursos@esgfuturo.com",
                "cursos": [
                    {"nome_curso": "ESG Fundamentals", "horas": "18h", "professor": "Roberto Padrão", "descricao": "Fundamentos de Governança Ambiental."},
                    {"nome_curso": "ESG Prático", "horas": "22h", "professor": "Eng. Sofia Luz", "descricao": "Aplicação prática de normas ESG."},
                    {"nome_curso": "Impacto Socioambiental", "horas": "30h", "professor": "Lucas Social", "descricao": "Medindo impacto na sociedade."}
                ]
            }
        ]

        # --- DADOS DOS PROFISSIONAIS ---
        st.session_state.profissionais = [
            # Perfil principal que usaremos para teste
            {
                "id": 999, "nome": "Rafael Martins", "cpf": "32211899022", "data_nascimento": "10/10/1997",
                "cidade": "São Paulo", "trilha": "Gestão", "cargo": "Analista Jr", "email": "rafael.martins@email.com",
                "experiencia": "Busco transição para área verde.",
                "cursos_concluidos": ["GreenOps Básico"],
                "cursos_em_andamento": ["ESG Fundamentals", "Operações Circulares"]
            },
            # Outros profissionais para popular as listas das cooperativas
            {
                "id": 101, "nome": "Ana Beatriz Souza", "cpf": "28411287059", "data_nascimento": "12/08/1998",
                "cidade": "São Paulo", "trilha": "Operacional", "cargo": "Assistente de Reaproveitamento", "email": "ana.souza@email.com",
                "experiencia": "3 anos na área.",
                "cursos_concluidos": ["GreenOps Básico"],
                "cursos_em_andamento": ["ESG Fundamentals", "Operações Circulares"]
            },
            {
                "id": 102, "nome": "João Ricardo Pereira", "cpf": "10388422006", "data_nascimento": "03/11/1996",
                "cidade": "São Paulo", "trilha": "Sustentabilidade", "cargo": "Auxiliar de Sustentabilidade", "email": "joao.pereira@email.com",
                "experiencia": "Experiência em triagem.",
                "cursos_concluidos": ["ESG Fundamentals"],
                "cursos_em_andamento": ["GreenOps Básico", "Operações Circulares"]
            },
            {
                "id": 103, "nome": "Marcos André Lima", "cpf": "40011299000", "data_nascimento": "27/05/2000",
                "cidade": "São Paulo", "trilha": "Operacional", "cargo": "Auxiliar Operacional", "email": "marcos.lima@email.com",
                "experiencia": "Iniciante.",
                "cursos_concluidos": [],
                "cursos_em_andamento": ["GreenOps Básico", "ESG Fundamentals"]
            },
            {
                "id": 201, "nome": "Carla Regina Mendes", "cpf": "11920054010", "data_nascimento": "08/01/1997",
                "cidade": "Campinas", "trilha": "Triagem", "cargo": "Assistente de Centro de Triagem", "email": "carla.mendes@email.com",
                "experiencia": "Líder de equipe.",
                "cursos_concluidos": ["GreenOps Básico"],
                "cursos_em_andamento": ["Gestão de Resíduos Urbanos", "ESG Prático"]
            },
            {
                "id": 202, "nome": "Tiago Alexandre Rocha", "cpf": "05592199060", "data_nascimento": "15/09/1995",
                "cidade": "Campinas", "trilha": "Processos", "cargo": "Auxiliar de Processos Verdes", "email": "tiago.rocha@email.com",
                "experiencia": "Técnico em logística.",
                "cursos_concluidos": ["ESG Fundamentals"],
                "cursos_em_andamento": ["ESG Prático", "Operações Circulares"]
            },
            {
                "id": 203, "nome": "Fernanda Alves Dias", "cpf": "33100988048", "data_nascimento": "04/03/1999",
                "cidade": "Campinas", "trilha": "Operações", "cargo": "Assistente de Operações", "email": "fernanda.dias@email.com",
                "experiencia": "Foco em impacto social.",
                "cursos_concluidos": ["ESG Fundamentals", "GreenOps Básico"],
                "cursos_em_andamento": ["Impacto Socioambiental"]
            }
        ]

        # --- DADOS DAS COOPERATIVAS ---
        st.session_state.cooperativas = [
            {
                "id": 1,
                "nome": "Cooperativa Verde Circular",
                "cnpj": "12345678000190",
                "email": "contato@verdecircular.org",
                "area_atuacao": "Reciclagem Geral",
                "descricao": "Focada em reaproveitamento na zona sul de SP.",
                "cursos_adotados": ["GreenOps Básico", "ESG Fundamentals"],
                # Lista de IDs para relacionar com a lista de profissionais acima
                "profissionais_associados_ids": [101, 102, 103],
                "vagas": [
                    {"id_vaga": 1, "titulo": "Operador de Triagem", "requisito": "GreenOps Básico", "salario": "R$ 2.100", "status": "Aberta"},
                    {"id_vaga": 2, "titulo": "Auxiliar de Coleta", "requisito": "ESG Fundamentals", "salario": "R$ 2.000", "status": "Aberta"}
                ],
                # Lista de inscrições que aparecerão no painel da cooperativa
                "inscricoes": [
                    {"id_candidato": 501, "nome_candidato": "Gabriel Moura", "vaga_titulo": "Operador de Triagem", "status": "Pendente"},
                    {"id_candidato": 502, "nome_candidato": "Larissa Costa", "vaga_titulo": "Auxiliar de Coleta", "status": "Pendente"}
                ]
            },
            {
                "id": 2,
                "nome": "EcoTriagem Brasil",
                "cnpj": "21559333000111",
                "email": "contato@ecotriagembrasil.org",
                "area_atuacao": "Logística Reversa",
                "descricao": "Especialista em logística reversa em Campinas.",
                "cursos_adotados": ["Gestão de Resíduos Urbanos", "ESG Prático"],
                "profissionais_associados_ids": [201, 202, 203],
                "vagas": [
                    {"id_vaga": 3, "titulo": "Técnico de Separação", "requisito": "Gestão de Resíduos Urbanos", "salario": "R$ 2.400", "status": "Aberta"},
                    {"id_vaga": 4, "titulo": "Auxiliar de Manutenção", "requisito": "ESG Prático", "salario": "R$ 2.150", "status": "Aberta"}
                ],
                "inscricoes": [
                    {"id_candidato": 601, "nome_candidato": "Rodrigo Ferreira", "vaga_titulo": "Técnico de Separação", "status": "Pendente"},
                    {"id_candidato": 602, "nome_candidato": "Paula Nascimento", "vaga_titulo": "Auxiliar de Manutenção", "status": "Pendente"}
                ]
            }
        ]
        
        # Flag para indicar que os dados iniciais foram carregados
        st.session_state.dados_carregados = True
        
        # Inicializa variáveis de controle de navegação
        if "usuario_selecionado" not in st.session_state:
            st.session_state.usuario_selecionado = None
        if "tipo_usuario" not in st.session_state:
            st.session_state.tipo_usuario = None
        if "aviso_sucesso" not in st.session_state:
            st.session_state.aviso_sucesso = None

# --- 3. TELAS E MENUS DO SISTEMA ---

def menu_profissional():
    """Exibe a área logada do profissional."""
    usuario = st.session_state.usuario_selecionado
    
    # Barra lateral com resumo e botão de sair
    st.sidebar.header(f"Olá, {usuario['nome']}")
    st.sidebar.info("Perfil: Profissional")
    if st.sidebar.button("Voltar / Trocar Perfil"):
        st.session_state.usuario_selecionado = None
        st.rerun()
    
    # Exibe mensagens de sucesso (se houver) no topo da tela
    if "aviso_sucesso" in st.session_state and st.session_state.aviso_sucesso:
        st.success(st.session_state.aviso_sucesso)

    # Menu de navegação usando Radio Button Horizontal
    # Usamos 'on_change=limpar_aviso' para apagar mensagens antigas ao trocar de tela
    aba = st.radio(
        "Navegação", 
        ["Meu Perfil", "Cursos Disponíveis", "Vagas & Candidaturas", "Minhas Inscrições"], 
        horizontal=True, 
        label_visibility="collapsed",
        key="nav_prof",
        on_change=limpar_aviso
    )

    # --- TELA: PERFIL ---
    if aba == "Meu Perfil":
        st.header("Meus Dados")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Nome:** {usuario['nome']}")
            st.write(f"**CPF:** {formatar_cpf(usuario['cpf'])}")
            st.write(f"**Cidade:** {usuario['cidade']}")
        with col2:
            st.write(f"**Cargo:** {usuario['cargo']}")
            st.write(f"**Trilha:** {usuario['trilha']}")
            st.write(f"**Email:** {usuario['email']}")
        
        st.markdown("---")
        st.subheader("Minha Educação")
        
        col_edu1, col_edu2 = st.columns(2)
        with col_edu1:
            st.success("✅ **Cursos Concluídos:**")
            if usuario['cursos_concluidos']:
                for c in usuario['cursos_concluidos']:
                    st.write(f"- {c}")
            else:
                st.write("Nenhum curso concluído ainda.")

        with col_edu2:
            st.info("🔄 **Cursos em Andamento:**")
            if usuario['cursos_em_andamento']:
                for c in usuario['cursos_em_andamento']:
                    st.write(f"- {c}")
            else:
                st.write("Nenhum curso em andamento.")

    # --- TELA: CURSOS (CATÁLOGO) ---
    elif aba == "Cursos Disponíveis":
        st.header("Catálogo de Cursos")
        
        # Itera sobre todas as instituições e seus cursos
        for instituicao in st.session_state.instituicoes:
            st.subheader(f"🏛️ {instituicao['nome']}")
            for curso in instituicao['cursos']:
                nome_curso = curso['nome_curso']
                
                with st.expander(f"{nome_curso} ({curso['horas']})"):
                    st.write(f"**Professor:** {curso['professor']}")
                    st.write(f"**Descrição:** {curso['descricao']}")
                    
                    # Lógica para exibir os botões corretos dependendo do status do curso
                    if nome_curso in usuario['cursos_concluidos']:
                        st.write("✅ **Você já concluiu este curso.**")
                    
                    elif nome_curso in usuario['cursos_em_andamento']:
                        # Botão para finalizar o curso
                        if st.button(f"Concluir Curso", key=f"concluir_{nome_curso}"):
                            usuario['cursos_em_andamento'].remove(nome_curso)
                            usuario['cursos_concluidos'].append(nome_curso)
                            st.session_state.aviso_sucesso = f"Parabéns! Curso '{nome_curso}' concluído."
                            st.rerun()
                    else:
                        # Botão para iniciar o curso
                        if st.button(f"Iniciar Curso", key=f"iniciar_{nome_curso}"):
                            usuario['cursos_em_andamento'].append(nome_curso)
                            st.session_state.aviso_sucesso = f"Você iniciou o curso '{nome_curso}'."
                            st.rerun()

    # --- TELA: VAGAS ---
    elif aba == "Vagas & Candidaturas":
        st.header("Vagas nas Cooperativas")
        
        for coop in st.session_state.cooperativas:
            st.subheader(f"🏢 {coop['nome']}")
            
            for vaga in coop['vagas']:
                if vaga['status'] == "Aberta":
                    with st.container(border=True):
                        col_vaga1, col_vaga2 = st.columns([3, 1])
                        with col_vaga1:
                            st.markdown(f"### {vaga['titulo']}")
                            st.markdown(f"**Salário:** {vaga['salario']}")
                            st.markdown(f"**Requisito:** Curso de *{vaga['requisito']}*")
                        
                        with col_vaga2:
                            # Verifica se o usuário JÁ se candidatou antes
                            ja_candidatou = False
                            for inscricao in coop['inscricoes']:
                                if inscricao['id_candidato'] == usuario['id'] and inscricao['vaga_titulo'] == vaga['titulo']:
                                    ja_candidatou = True
                                    break
                            
                            if ja_candidatou:
                                st.warning("Já candidatado")
                            else:
                                # Verifica se o usuário TEM o curso exigido
                                if vaga['requisito'] in usuario['cursos_concluidos']:
                                    if st.button("Candidatar-se", key=f"cand_{coop['id']}_{vaga['id_vaga']}"):
                                        # Cria o registro da inscrição na lista da cooperativa
                                        nova_inscricao = {
                                            "id_candidato": usuario['id'],
                                            "nome_candidato": usuario['nome'],
                                            "vaga_titulo": vaga['titulo'],
                                            "status": "Pendente"
                                        }
                                        coop['inscricoes'].append(nova_inscricao)
                                        st.session_state.aviso_sucesso = "Currículo enviado com sucesso!"
                                        st.rerun()
                                else:
                                    st.error("Requisito pendente")

    # --- TELA: HISTÓRICO ---
    elif aba == "Minhas Inscrições":
        st.header("Minhas Inscrições")
        encontrou = False
        
        # Procura inscrições deste usuário em todas as cooperativas
        for coop in st.session_state.cooperativas:
            for inscricao in coop['inscricoes']:
                if inscricao['id_candidato'] == usuario['id']:
                    encontrou = True
                    status = inscricao['status']
                    
                    # Define a cor do texto baseada no status
                    cor = "blue"
                    if status == "Aceita": cor = "green"
                    if status == "Recusada": cor = "red"
                    
                    st.markdown(f"**Vaga:** {inscricao['vaga_titulo']} | **Local:** {coop['nome']} | **Status:** :{cor}[{status}]")
        
        if not encontrou:
            st.info("Você ainda não se candidatou a nenhuma vaga.")

def menu_cooperativa():
    """Exibe a área logada da cooperativa."""
    coop = st.session_state.usuario_selecionado
    
    st.sidebar.header(f"Gestão: {coop['nome']}")
    st.sidebar.info("Perfil: Cooperativa")
    if st.sidebar.button("Voltar / Trocar Perfil"):
        st.session_state.usuario_selecionado = None
        st.rerun()
    
    # Exibe aviso persistente
    if "aviso_sucesso" in st.session_state and st.session_state.aviso_sucesso:
        st.success(st.session_state.aviso_sucesso)

    # Navegação horizontal
    aba = st.radio(
        "Navegação", 
        ["Perfil", "Profissionais Associados", "Vagas & Inscrições", "Cursos Adotados"], 
        horizontal=True,
        label_visibility="collapsed",
        key="nav_coop",
        on_change=limpar_aviso
    )
    
    # --- TELA: PERFIL COOP ---
    if aba == "Perfil":
        st.header("Dados da Cooperativa")
        st.write(f"**Razão Social:** {coop['nome']}")
        st.write(f"**CNPJ:** {formatar_cnpj(coop['cnpj'])}")
        st.write(f"**Área:** {coop['area_atuacao']}")
        st.write(f"**Email:** {coop['email']}")
        st.write(f"**Descrição:** {coop['descricao']}")
        
    # --- TELA: EQUIPE ---
    elif aba == "Profissionais Associados":
        st.header("Nossa Equipe")
        
        # Busca os detalhes dos profissionais associados usando os IDs
        profissionais_encontrados = []
        for prof_id in coop['profissionais_associados_ids']:
            for p in st.session_state.profissionais:
                if p['id'] == prof_id:
                    profissionais_encontrados.append(p)
                    break
        
        if profissionais_encontrados:
            for prof in profissionais_encontrados:
                with st.expander(f"{prof['nome']} - {prof['cargo']}"):
                    st.write(f"**Cidade:** {prof['cidade']}")
                    st.write(f"**Cursos Concluídos:** {', '.join(prof['cursos_concluidos'])}")
                    st.write(f"**Cursos em Andamento:** {', '.join(prof['cursos_em_andamento'])}")
        else:
            st.write("Nenhum profissional associado no momento.")
            
    # --- TELA: VAGAS E CANDIDATURAS ---
    elif aba == "Vagas & Inscrições":
        st.header("Gestão de Candidaturas")
        
        for vaga in coop['vagas']:
            st.subheader(f"Vaga: {vaga['titulo']} ({vaga['status']})")
            
            # Filtra apenas as inscrições desta vaga específica que estão pendentes
            candidatos_pendentes = []
            for insc in coop['inscricoes']:
                if insc['vaga_titulo'] == vaga['titulo'] and insc['status'] == "Pendente":
                    candidatos_pendentes.append(insc)
            
            if candidatos_pendentes:
                st.write("📥 **Candidaturas Pendentes:**")
                # Usamos enumerate para saber o índice correto e alterar a lista original
                for i, insc in enumerate(coop['inscricoes']):
                    if insc['vaga_titulo'] == vaga['titulo'] and insc['status'] == "Pendente":
                        col1, col2, col3 = st.columns([4, 1, 1])
                        with col1:
                            st.write(f"Candidato: **{insc['nome_candidato']}**")
                        with col2:
                            if st.button("✅ Aceitar", key=f"aceitar_{vaga['id_vaga']}_{i}"):
                                coop['inscricoes'][i]['status'] = "Aceita"
                                st.session_state.aviso_sucesso = f"Entraremos em contato com o candidato {insc['nome_candidato']}."
                                st.rerun()
                        with col3:
                            if st.button("❌ Recusar", key=f"recusar_{vaga['id_vaga']}_{i}"):
                                coop['inscricoes'][i]['status'] = "Recusada"
                                st.session_state.aviso_sucesso = f"Candidatura de {insc['nome_candidato']} foi recusada."
                                st.rerun()
            else:
                st.write("Nenhuma candidatura pendente.")
            st.divider()
            
    # --- TELA: CURSOS REQUISITOS ---
    elif aba == "Cursos Adotados":
        st.header("Matriz de Capacitação")
        st.write("Cursos que exigimos para nossas vagas:")
        for c in coop['cursos_adotados']:
            st.write(f"🔹 {c}")
            
        st.divider()
        st.subheader("Adicionar Novo Curso")
        
        # Cria uma lista única com todos os cursos de todas as instituições para o selectbox
        todos_cursos = []
        for inst in st.session_state.instituicoes:
            for c in inst['cursos']:
                if c['nome_curso'] not in todos_cursos:
                    todos_cursos.append(c['nome_curso'])
        
        novo_curso = st.selectbox("Selecione um curso para adotar:", todos_cursos)
        
        if st.button("Adicionar Curso"):
            if novo_curso not in coop['cursos_adotados']:
                coop['cursos_adotados'].append(novo_curso)
                st.session_state.aviso_sucesso = "Curso adicionado com sucesso!"
                st.rerun()
            else:
                st.warning("Este curso já está na lista.")

def menu_instituicao():
    """Exibe a área logada da instituição de ensino."""
    inst = st.session_state.usuario_selecionado
    
    st.sidebar.header(f"{inst['nome']}")
    st.sidebar.info("Perfil: Instituição de Ensino")
    if st.sidebar.button("Voltar / Trocar Perfil"):
        st.session_state.usuario_selecionado = None
        st.rerun()

    aba = st.radio(
        "Navegação", 
        ["Cursos Ofertados", "Alunos Formados", "Parcerias (Adoção)"], 
        horizontal=True,
        label_visibility="collapsed",
        key="nav_inst",
        on_change=limpar_aviso
    )
    
    # --- TELA: CURSOS DA INSTITUIÇÃO ---
    if aba == "Cursos Ofertados":
        st.header("Nossos Cursos")
        for curso in inst['cursos']:
            with st.expander(f"{curso['nome_curso']} ({curso['horas']})"):
                st.write(f"**Professor:** {curso['professor']}")
                st.write(f"**Descrição:** {curso['descricao']}")
                
    # --- TELA: ALUNOS ---
    elif aba == "Alunos Formados":
        st.header("Profissionais Certificados")
        
        meus_cursos_nomes = []
        for c in inst['cursos']:
            meus_cursos_nomes.append(c['nome_curso'])
            
        for curso_nome in meus_cursos_nomes:
            st.subheader(f"🎓 {curso_nome}")
            encontrou_aluno = False
            # Varre todos os profissionais do sistema para ver quem fez este curso
            for p in st.session_state.profissionais:
                if curso_nome in p['cursos_concluidos']:
                    st.write(f"- **{p['nome']}** ({p['cidade']})")
                    encontrou_aluno = True
            
            if not encontrou_aluno:
                st.write("Nenhum aluno concluiu este curso ainda.")
                
    # --- TELA: PARCERIAS ---
    elif aba == "Parcerias (Adoção)":
        st.header("Cooperativas Parceiras")
        st.write("Cooperativas que utilizam nossos cursos como requisito:")
        
        meus_cursos_nomes = []
        for c in inst['cursos']:
            meus_cursos_nomes.append(c['nome_curso'])
            
        # Verifica se as cooperativas tem algum dos meus cursos na lista de adotados
        for coop in st.session_state.cooperativas:
            cursos_em_comum = []
            for c_adotado in coop['cursos_adotados']:
                if c_adotado in meus_cursos_nomes:
                    cursos_em_comum.append(c_adotado)
            
            if cursos_em_comum:
                with st.expander(f"{coop['nome']}"):
                    st.write("**Utiliza os cursos:**")
                    for c in cursos_em_comum:
                        st.write(f"- {c}")

# --- 4. FLUXO PRINCIPAL (MAIN) ---

def main():
    """Função principal que controla qual tela mostrar."""
    
    # 1. Garante que os dados fictícios estejam carregados
    inicializar_dados_demo()
    
    # 2. Verifica se temos um usuário "logado" na demo
    if st.session_state.usuario_selecionado is None:
        
        # TELA INICIAL (SELEÇÃO DE PERFIL)
        st.title("🔄 ReWork Circular — Acesso de Demonstração")
        st.markdown("Bem-vindo ao ambiente de simulação. Escolha um perfil para testar o sistema.")
        
        col_esq, col_dir = st.columns([1, 2])
        
        with col_esq:
            st.subheader("Como deseja acessar?")
            tipo_acesso = st.radio(
                "Selecione o tipo de perfil:",
                ["Profissional", "Cooperativa", "Instituição de Ensino"]
            )
            
            if st.button("Resetar Dados da Demo"):
                # Limpa a memória para reiniciar os dados originais
                st.session_state.clear()
                st.rerun()
        
        with col_dir:
            st.subheader(f"Selecione o {tipo_acesso}")
            
            if tipo_acesso == "Profissional":
                # Monta dicionário manualmente: chave = nome, valor = dados completos
                opcoes = {}
                for p in st.session_state.profissionais:
                    opcoes[p['nome']] = p
                
                escolha = st.selectbox("Quem é você?", list(opcoes.keys()))
                
                if st.button("Entrar como Profissional"):
                    st.session_state.usuario_selecionado = opcoes[escolha]
                    st.session_state.tipo_usuario = "Profissional"
                    st.rerun()
                    
            elif tipo_acesso == "Cooperativa":
                # Monta dicionário manualmente para Cooperativas
                opcoes = {}
                for c in st.session_state.cooperativas:
                    opcoes[c['nome']] = c

                escolha = st.selectbox("Qual cooperativa?", list(opcoes.keys()))
                
                if st.button("Entrar como Cooperativa"):
                    st.session_state.usuario_selecionado = opcoes[escolha]
                    st.session_state.tipo_usuario = "Cooperativa"
                    st.rerun()
                    
            elif tipo_acesso == "Instituição de Ensino":
                # Monta dicionário manualmente para Instituições
                opcoes = {}
                for i in st.session_state.instituicoes:
                    opcoes[i['nome']] = i

                escolha = st.selectbox("Qual instituição?", list(opcoes.keys()))
                
                if st.button("Entrar como Instituição"):
                    st.session_state.usuario_selecionado = opcoes[escolha]
                    st.session_state.tipo_usuario = "Instituição"
                    st.rerun()

    else:
        # 3. Se já estiver logado, redireciona para o menu correto
        tipo = st.session_state.tipo_usuario
        
        if tipo == "Profissional":
            menu_profissional()
        elif tipo == "Cooperativa":
            menu_cooperativa()
        elif tipo == "Instituição":
            menu_instituicao()

# Garante que o script rode apenas se executado diretamente
if __name__ == "__main__":
    main()