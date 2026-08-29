[🇪🇸 Español](case_01_tactical_decision_support.md) | [🇬🇧 English](case_01_tactical_decision_support_EN.md)

# CASO DE ESTUDIO 1: DEL DATO A LA PIZARRA — SOPORTE TÁCTICO Y PREPARACIÓN PREPARTIDO
## International Basketball Analytics (2005–2024)

> **Perfil de Audiencia**: *Head Coaches, Entrenadores Ayudantes, Coordinadores de Vídeo y Secretarías Técnicas.*  
> **Pregunta Clave**: *¿Cómo traducimos estadísticas complejas y tendencias del rival en un informe ejecutivo de página y media sin saturar al cuerpo técnico?*

---

## 1. El Problema en el Baloncesto de Alta Competición

En una semana de competición o en un torneo de selecciones, el cuerpo técnico dispone de menos de 48 horas entre partidos. Los informes estadísticos tradicionales de 30 páginas suelen acabar en la papelera porque:
1. Contienen **demasiado ruido** y métricas descontextualizadas del ritmo de juego.
2. Presentan **sesgo retrospectivo**: juzgan una decisión únicamente por si el último tiro entró o no.
3. No alertan sobre **contradicciones tácticas** entre las cifras agregadas y lo que sucede realmente en la cinta de vídeo.

---

## 2. La Solución Construida

Desarrollamos un generador determinista de **Briefs Prepartido de 1.5 páginas** estructurado en 3 bloques procesables:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ESTRUCTURA DEL BRIEF PREPARTIDO EJECUTIVO                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. IDENTIDAD DE RITMO Y FOUR FACTORS (Dean Oliver)                                     │
│    • Posesiones estimadas y Net Rating frente a la media del torneo.                   │
│    • Cuadrante de eficiencia de tiro (eFG%), pérdidas (TOV%), rebote (ORB%) y FTR.     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. PERFILES INDIVIDUALES Y MAPAS DE TIRO AJUSTADOS                                     │
│    • Los 3 generadores principales del rival con sus arquetipos funcionales.           │
│    • True Shooting % ajustado por contracción bayesiana (λ=0.75) y distribución de tiro.│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. CONSIGNAS TÁCTICAS Y GUÍA PARA LA SESIÓN DE SCOUTING                               │
│    • Cruce entre diferenciales de Four Factors y tendencias espaciales de tiro.        │
│    • Detección de vulnerabilidades defensivas (ej. defensa hundida en pick-and-roll).  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Evidencia Real: Aplicación a la Final de Pekín 2008 (España vs. EE. UU.)

- **Contexto**: España había perdido en la fase de grupos por 37 puntos ($82\text{–}119$) ante el *Redeem Team*.
- **Señal Cuantitativa**: En posesiones de media pista (5c5 en estático), España superaba a EE. UU. en Net Rating ($+4.2$) gracias a la ventaja interior de Pau y Marc Gasol. La sangría procedía de las transiciones tras pérdida ($1.25$ PPP concedidos).
- **Hipótesis Táctica**: Los pívots estadounidenses realizaban una defensa muy hundida en la pintura para tapar penetraciones, concediendo tiros liberados en pick-and-pop a interiores con rango de tiro exterior.
- **Ajustes en el Brief**:
  1. *Ritmo*: Bajar el partido a menos de 72 posesiones mediante posesiones controladas.
  2. *Defensa*: Plantear zona 2-3 tras canasta propia para frenar el contraataque rápido.
  3. *Ataque*: Castigar la defensa hundida con tiros exteriores de Pau Gasol, Marc Gasol y Jorge Garbajosa.
- **Resultado en Pista**: España ejecutó el plan, recortó la distancia a 4 puntos ($108\text{–}104$) a falta de $2:20$ y compitió en una de las finales más ajustadas de la historia olímpica ($107\text{–}118$).

---

## 4. Qué Demuestra este Caso de Estudio

- **Enfoque Data-First**: El proyecto no depende de anotaciones manuales de vídeo; utiliza datos cuantitativos rigurosos para orientar al cuerpo técnico.
- Capacidad de **comunicación directa con entrenadores** sin tecnicismos matemáticos innecesarios.
- Enfoque pragmático centrado en el **soporte a decisiones y preparación prepartido**.
