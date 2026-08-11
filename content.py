"""
All editable content for the site lives here.

To update the site: edit the values below, then run:
    python build.py

Nothing else needs to change. Every dict/list here maps directly
to a section on the page.
"""

SITE = {
    "title": "Grold Otieno Mboya",
    "description": "Grold Otieno Mboya — research in causal inference, "
                    "topological data analysis, and foundation model evaluation.",
    "name": "Grold Otieno Mboya",
    "role": "causal inference · topology · foundation model evaluation",
    "thesis": (
        "I'm a researcher and engineer working on causal inference and topological "
        "data analysis, applied to foundation model evaluation, out-of-distribution "
        "detection, and benchmark design — building open diagnostics that surface "
        "where adaptive, continuously-learning systems quietly fail."
    ),
    "email": "groldotieno97@gmail.com",
    "orcid_url": "https://orcid.org/0009-0005-9102-4028",
    "github_url": "https://github.com/Grolds-Code",
    # Optional — leave as "" to hide. Fill in if you have a Google Scholar or
    # Semantic Scholar profile; reviewers often check citation counts there.
    "scholar_url": "",
    "cv_url": "#",  # replace with a real link once the CV PDF is hosted
    "location": "Kisumu, Kenya",
    # Update these once the personal domain is registered and the site is live.
    "canonical_url": "https://example.com/",
    "og_image_url": "https://example.com/og-image.png",
}

RESEARCH_STATEMENT = [
    "Most model evaluation asks whether a model is right on average. I ask where it "
    "quietly breaks — under distribution shift, in the geometry of its latent space, "
    "or at the seam between training and deployment data.",

    "Persistent homology gives a way to characterize the shape of that breakdown. "
    "Causal inference gives a way to tell a genuine failure mode apart from a "
    "sampling or reporting artifact that only looks like one.",

    "That runs through three settings I work in now: stress-testing a mid-size "
    "language model for out-of-distribution blind spots, building diagnostics for "
    "continuous-learning systems whose training distribution shifts during "
    "deployment, and applying topological probes to protein foundation models and "
    "epidemiological surveillance data. The throughline is empirical evaluation "
    "and safety alignment for adaptive, large-scale models.",
]

PUBLICATIONS = [
    {
        "title": "DirSNN: A Memory-Safe, Harmonic-Aware Architecture for Directed Simplicial Complexes",
        "venue": "SSRN (preprint), 2026",
        "desc": "A memory-safe directed simplicial neural architecture integrated into "
                "TopoBench, improving OOD generalization without dense gradient materialization.",
        "link_label": "ssrn · abstract_id=7122398",
        "link_url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7122398",
    },
    {
        "title": "Why Invariant Risk Minimization Fails on Tabular Data: A Gradient Variance Solution",
        "venue": "medRxiv (preprint), 2026",
        "desc": "Identifies a structural failure mode in causal invariance algorithms and "
                "proposes a gradient variance correction for cross-environment generalization.",
        "link_label": "doi.org/10.64898/2026.04.09.26350513",
        "link_url": "https://doi.org/10.64898/2026.04.09.26350513",
    },
    {
        "title": "Topological Probing of Latent Space Geometry in Protein Foundation Models under Distribution Shift",
        "venue": "Research Square (preprint), 2026",
        "desc": "Uses persistent homology to characterize distributional shift in ESM-2 "
                "representations, establishing layer-specific topological diagnostics.",
        "link_label": "doi.org/10.21203/rs.3.rs-9767602/v1",
        "link_url": "https://doi.org/10.21203/rs.3.rs-9767602/v1",
    },
    {
        "title": "Topological Causal Graph Neural Networks for Detecting Structural Voids in Epidemiological Surveillance",
        "venue": "SSRN (preprint), 2026",
        "desc": "Introduces TCGNN, integrating computational topology and causal calculus "
                "to detect structural reporting voids in health surveillance data.",
        "link_label": "ssrn · abstract_id=6842658",
        "link_url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6842658",
    },
    {
        "title": "An Integrated Analytical Framework for Gender-Based Violence Research",
        "venue": "medRxiv (preprint), 2025",
        "desc": "A simulation study combining machine learning with causal inference to "
                "disentangle structural drivers of GBV from reporting artifacts.",
        "link_label": "doi.org/10.64898/2025.12.15.25342247",
        "link_url": "https://doi.org/10.64898/2025.12.15.25342247",
    },
]

DEMOS_INTRO = (
    "Three LoRA adapters from the Adaption Labs closed beta, trained on "
    "programmatically generated ground truth, each with a public demo."
)

DEMOS = [
    {
        "tag": "Llama-4-Scout-17B · math & code",
        "title": "Directed simplicial homology reasoning",
        "desc": "Facet validity checking, orientation-sign composition, boundary matrix "
                "rank, and Betti number computation via exact linear algebra.",
        "stats": [("23% → 77%", "held-out"), ("36% → 64%", "math, p<0.01")],
        "links": [("demo", "#"), ("model", "#"), ("dataset", "#")],
    },
    {
        "tag": "Llama 3.3 70B · personal finance",
        "title": "Financial reasoning QA",
        "desc": "Debt payoff, retirement and loan math, opportunity cost, plus a Kenya/East "
                "Africa slice on PAYE, SACCO loans, and chama timing.",
        "stats": [("10% → 90%", "overall"), ("11% → 89%", "finance")],
        "links": [("demo", "#"), ("model", "#"), ("dataset", "#")],
    },
    {
        "tag": "Llama 3.3 70B · agriculture",
        "title": "Crop diagnosis reasoning",
        "desc": "Differential diagnosis of confusable crop conditions — weighs evidence, "
                "names ruled-out alternatives, states the confirming detail.",
        "stats": [("19% → 81%", "overall"), ("17% → 84%", "agriculture")],
        "links": [("demo", "#"), ("model", "#"), ("dataset", "#")],
    },
]

OPEN_SOURCE = [
    {
        "title": "DirSNN — TDL Challenge 2026, Track 2",
        "meta": "github.com/Grolds-Code",
        "meta_url": None,
        "desc": "Asymmetric adjacency operators in place of symmetric Hodge Laplacians; "
                "8.7× GPU memory reduction at 1.3M triangles via active simplicial "
                "sparsification, integrated into TopoBench.",
    },
    {
        "title": "TDA Engine",
        "meta": "R / Shiny → streaming microservice",
        "meta_url": "https://gro7d.shinyapps.io/TDA-Engine-Preview/",
        "desc": "Uses persistent homology to distinguish structural voids from natural "
                "absence in high-dimensional data. In progress: rebuilding for "
                "real-time, low-latency inference.",
    },
    {
        "title": "Qwen-1.5B epistemic TDA blindspots dataset",
        "meta": "huggingface.co/datasets/Gro97",
        "meta_url": "https://huggingface.co/datasets/Gro97/qwen-1.5b-epi-tda-blindspots",
        "desc": "Full OOD evaluation dataset from the Fatima Institute fellowship, "
                "published with a fine-tuning strategy to mitigate the spurious "
                "correlations it identifies.",
    },
]

# Fellowships and education, deliberately combined — degree entries name the
# degree only, no institution.
EXPERIENCE = [
    {
        "title": "NIXQUE — Co-Founder &amp; CTO",
        "meta": "2023 – present",
        "desc": "Sole technical lead for a full-stack technology startup; product "
                "strategy, system architecture, and deployment pipelines in "
                "TypeScript, React, and FastAPI.",
    },
]

FELLOWSHIPS = [
    {
        "title": "Adaption Labs — Early Access Builder",
        "meta": "2026 – present",
        "desc": "Closed beta cohort running OOD evaluations on a continuous-learning "
                "architecture; direct collaboration with founders on the pre-release roadmap.",
    },
    {
        "title": "Fatima Institute — Research Fellow",
        "meta": "May – Dec 2026",
        "desc": "Selected from 700+ applicants to stress-test Qwen-1.5B for OOD failure "
                "modes under distribution shift.",
    },
    {
        "title": "MSc, Financial Engineering",
        "meta": "2026 – present",
        "desc": None,
    },
    {
        "title": "MSc, Epidemiology and Biostatistics",
        "meta": "2025 – 2026 · 6 distinctions, 6 credits",
        "desc": "Thesis: modeling the impact of BMI on hypertension risk among people "
                "living with HIV on ART in Kisumu County, using Bayesian hierarchical "
                "spatial models.",
    },
    {
        "title": "KEMRI-CGHR — Bioinformatics &amp; Research Intern",
        "meta": "2023 – 2024",
        "desc": "Data pipelines for high-dimensional biological datasets across 12 "
                "sentinel sites; SOPs adopted by the vector biology unit.",
    },
]

RECOGNITION = [
    {
        "title": "Prototypes for Humanity 2026 — Dubai Future Solutions Summit",
        "meta": "Nov 2026 · Jumeirah Emirates Towers, Dubai",
        "desc": "CausTab-Global: A Deployment Audit Tool for Clinical AI Across Health "
                "Systems selected to exhibit at the 2026 summit.",
    },
    {
        "title": "2nd Primary Health Care Congress — Oral Presentation",
        "meta": "Mar 2026 · Amref International University, Nairobi",
        "desc": 'Abstract accepted: "The PHC Predictive Intelligence Platform — Building '
                'Financial and Operational Resilience Through Anticipatory Primary '
                'Healthcare in Kenya."',
    },
]
