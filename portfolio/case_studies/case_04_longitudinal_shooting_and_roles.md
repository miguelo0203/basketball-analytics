[🇪🇸 Español](case_04_longitudinal_shooting_and_roles.md) | [🇬🇧 English](case_04_longitudinal_shooting_and_roles_EN.md)

# CASO DE ESTUDIO 4: ESTABILIDAD LONGITUDINAL, INFERENCIA EN R Y MINERÍA DE ROLES
## International Basketball Analytics (2005–2024)

> **Perfil de Audiencia**: *Scouts Profesionales, Directores Deportivos, Analistas Estadísticos y Desarrolladores R / Quarto.*  
> **Pregunta Clave**: *¿Cómo diferenciar la calidad real de un jugador de las rachas de tiro a corto plazo y mapear roles funcionales objetivos en el juego?*

---

## 1. El Reto de la Muestra Corta en Competiciones de Baloncesto

En un torneo internacional o serie de playoffs (6 a 9 partidos), un jugador que lanza $15/30$ en triples registra un aparente $50\%$. Si hubiera fallado 3 de esos tiros, su registro caería al $40\%$.
Juzgar el perfil de tiro de un atleta basándose en muestras tan reducidas lleva a sobrepagar contratos o plantear ajustes defensivos erróneos sobre varianza pura.

---

## 2. Inferencia Estadística en R e Invarianza de Métricas

Utilizando la capa estadística en R conectada directamente a DuckDB vía `DBI`:
1. **Análisis Longitudinal de 3.767 Campañas Cualificadas** ($\ge 40$ minutos jugados).
2. **Bandas de Confianza Bootstrap ($B=5.000$ iteraciones)**: Modelamos la incertidumbre de la métrica True Shooting ($TS\%$) a lo largo de las carreras de leyendas internacionales (Pau Gasol, Dirk Nowitzki, Rudy Fernández, Bogdan Bogdanović).
3. **Contracción Bayesiana ($\lambda = 0.75$)**: Suavizamos las estimaciones de tiro de torneos cortos hacia la media histórica ponderada por posesiones del jugador, logrando perfiles de tiro resistentes al ruido.

---

## 3. Minería de 6 Arquetipos Funcionales (K-Means++ & PCA)

Superamos las 5 posiciones tradicionales del baloncesto (del 1 al 5) mediante clustering no supervisado sobre 14 métricas normalizadas por 40 minutos (explicando $>60\%$ de varianza con los 3 primeros componentes principales):

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        LOS 6 ARQUETIPOS FUNCIONALES AUDITADOS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Primary Initiator  │ Generador principal de P&R, alto uso de balón y anotación.     │
│ 2. Floor Spacer       │ Tirador especialista exterior de alto volumen en catch-and-shoot│
│ 3. Interior Hub       │ Pívot receptor, finalizador en pintura y pasador desde poste.  │
│ 4. Floor General      │ Base director tradicional, bajo ratio de pérdidas y pase puro. │
│ 5. Defensive Anchor   │ Protector de aro, reboteador defensivo y finalizador de pick.  │
│ 6. Balanced Wing      │ Alero versátil 'two-way' de impacto múltiple defensivo y tiro. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Reporting Reproducible con Quarto CLI

Todo el análisis estadístico e inferencia no paramétrica se compila de forma automatizada en un informe interactivo HTML (`reports/exploratory_analysis.html`) y figuras vectoriales de 300 DPI utilizando la paleta institucional `theme_basketball_analytics()` en `ggplot2`.

---

## 5. Qué Demuestra este Caso de Estudio

- Competencia avanzada en **R, Tidyverse, Quarto y visualización técnica**.
- Comprensión profunda de la **varianza de tiro en baloncesto**.
- Capacidad para crear **herramientas de scouting y confección de plantilla** basadas en datos objetivos.
