---
name: pagina
description: Cria HTML local para a oferta aprovada ou a partir de referência, sem rastreadores ou publicação.
---

# Página local

Leia INSTRUCOES.md, perfil.json, projeto.md, oferta.md e visual/direcao-visual.md. Pergunte apenas o que falta e o destino real da chamada para ação. Sem direção visual, use direcao-visual e aprove a prévia primeiro.

**Oferta própria:** escreva texto com os dados aprovados e mostre para revisão. Sem prova autorizada, omita a seção; não simule depoimentos, urgência, preços, resultados ou clientes.

**Referência:** leia references/referencia.md. Observe estrutura/composição e reconstrua um HTML novo com identidade/conteúdo do participante. Não reutilize scripts, CSS remoto, pixels, cookies, formulários, contatos, imagens ou marcas da captura. A alternativa manual dispensa navegador automatizado.

Salve `<projeto>/site/index.html`, com CSS interno e PNG/JPEG/WebP locais autorizados. A rota padrão usa HTML/CSS sem scripts, SVG ativo, iframes, importações/fontes remotas ou frameworks. Links revisados fazem a navegação. Formulários são “Demonstração: não envia dados”, com controles desabilitados e sem action. Não prometa envio sem integração. JavaScript/integrações são etapa separada com revisão própria.

Confira com scripts/verificar_pagina.py se Python 3.10+ estiver disponível; --permitir-destino só lista URLs exatas confirmadas pelo dono. Não substitui revisão visual/de rede. Sem Python, use docs/PAGINA-LOCAL.md e registre checagem manual. Não execute HTML capturado de terceiros no vault.

Abra SOMENTE site em outra janela do VS Code e use Live Server. Nunca sirva o vault. Teste celular/desktop, teclado, contraste, destinos e rede sem rastreamento. Sem navegador disponível, peça a conferência ao participante e não afirme ter visto. Registre resultado/limites em pagina-revisao.md no projeto, vinculado em projeto.md.

Entregue caminho e como abrir localmente. Não acione /publicar, não proponha deploy automaticamente nem prometa link público.
