# Manutenção do template

Este documento vale quando a tarefa é desenvolver o kit, não personalizar o vault de um participante.

- Use branch e PR no repositório real. Não execute /setup com dados pessoais neste checkout, não remova .git e não envie notas de usuários.
- Instruções canônicas: .claude/skills/. Entradas do Codex: .agents/skills/, geradas por scripts/sincronizar_skills.py. Não duplique os corpos em .claude/commands/.
- Valide scripts com `python -m unittest discover -s tests -v` e descoberta com `python scripts/sincronizar_skills.py --check`. Testes usam diretórios temporários, nunca instalação real no computador.
- Dependências de design têm versão fixa e licenças em docs/DESIGN-E-LICENCAS.md. Não incorpore arquivos de repositórios sem licença presumindo permissão.
- Revise o diff antes de commit: sem perfil.json real, notas pessoais, .env, tokens ou configurações locais. A lista de ignorados ajuda, mas caminhos personalizados também precisam de revisão.
- Documente limites dos testes: fixtures verificam arquivos e invariantes, não provam qualidade da IA ou usabilidade com iniciante. Não declarar testes de macOS/humano que não ocorreram.
- Antes de atualizar manuais públicos de planejado para pronto, confira merge e download da branch padrão. PR disponível não significa main atualizado.
