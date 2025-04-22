---
layout: index
title: "FINOS AI Governance Framework"
subtitle: "A comprehensive collection of risks and mitigations that support on-boarding, development of, and running Generative AI solutions"
risk_order:
  - OP
  - SEC
  - RC
---

AI, especially Generative AI, is reshaping financial services, enhancing products, client interactions, and productivity. However, challenges like hallucinations and model unpredictability make safe deployment complex. Rapid advancements require flexible governance.

Financial institutions are eager to adopt AI but face regulatory hurdles. Existing frameworks may not address AI’s unique risks, necessitating an adaptive governance model for safe and compliant integration.

The following framework has been developed by [FINOS (Fintech Open Source Foundation)](https://www.finos.org/) members, providing  comprehensive catalogue or risks and associated mitigation. We suggest using our [heuristic risk identification framework](heuristic-assessment.html) to determine which risks are most relevant for a given use case.

## Risk Catalogue

<br/>
{% assign grouped_risks = site.risks | group_by: "type" %}

{% assign ordered_risks = "" | split: "," %}
{% for order in page.risk_order %}
  {% assign match = grouped_risks | where: "name", order | first %}
  {% if match %}
    {% assign ordered_risks = ordered_risks | push: match %}
  {% endif %}
{% endfor %}

{% for group in ordered_risks %}
<section class="mb-5">
    <h3 class="category-title mb-4">{{ site.risk_classification[group.name] }}</h3>
    <div class="row g-4">
        {% assign sorted_risks = group.items | sort: "sequence" %}
        {% for risk in sorted_risks %}
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="card index h-100 shadow-sm">
                <div class="card-body">
                    <div class="risk-id mb-2">
                      {% include risk-id.html risk=risk %}
                    </div>
                    <h3 class="card-title h5">{{ risk.title }}</h3>
                    <p class="card-text text-muted">{{ risk.content | strip_html | strip_newlines | split: " " | slice: 0, 10 | join: " " }} ...</p>
                    <a href="{{ risk.id }}.html" class="btn btn-outline-primary btn-sm stretched-link">Read more</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
{% endfor %}