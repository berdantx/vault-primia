# Abrir e conferir a página local

1. No VS Code, File → New Window. Depois File → Open Folder e escolha somente a pasta `site` do projeto, com index.html. Não abra o vault inteiro nessa janela de prévia.
2. Confira Live Server de Ritwick Dey instalado/habilitado. Abra index.html e clique Go Live, ou botão direito → Open with Live Server.
3. Leia a página no computador e numa largura de celular. Teste teclado, foco, contraste e todos os destinos. Ao salvar, a prévia deve atualizar.
4. Um formulário marcado demonstração não envia nada: controles desabilitados, sem endpoint. Confira que não sobrou contato, prova, marca ou rastreador de terceiros. Registre imagens e autorizações.
5. Para parar, clique no controle de porta/Live Server. O endereço é local, não publicação pública.

## Conferência opcional por script

Requer Python 3.10+ já disponível. Não é requisito para a aula:

```text
python scripts/verificar_pagina.py "projetos/meu-projeto/site/index.html"
```

Se há contato real revisado, acrescente `--permitir-destino "URL exata"` para cada destino autorizado. O comando só lê. Verifica a rota conservadora da oficina: sem scripts/iframes/SVG ativo, CSS externo/import/url(), formulários ativos, rastreadores conhecidos ou recursos remotos. Imagens locais PNG/JPEG/WebP são permitidas. Não é limpeza automática de captura ou auditoria completa; examinar a rede no navegador e revisar conteúdo continua necessário. Sem Python, confira manualmente esses itens e registre o limite.

A saída pode ser HTML simples aberto diretamente se Live Server não funcionar; atualização automática depende da extensão. Recursos dinâmicos/integrados ficam fora desse caminho.
