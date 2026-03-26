---
layout: default
title: "Propose a Use Case"
permalink: /propose/use-case/
---

<header class="py-5 bg-light border-bottom">
    <div class="container">
        <div class="mb-4">
            <a href="/use-cases/" class="text-decoration-none">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
                Back to Use Cases Catalogue
            </a>
        </div>
        <div class="d-flex align-items-center">
            <img src="/2025_AIGovernanceFramework_Icon.png" alt="AI Governance Framework Icon" style="height: 48px;" class="me-3 mb-0">
            <div>
                <h1 class="display-4 mb-1">Propose a Use Case</h1>
                <p class="lead mb-0">Fill in the details below. Clicking <strong>Submit Proposal</strong> will open a pre-filled GitHub Issue for review by the AIGF maintainers.</p>
            </div>
        </div>
    </div>
</header>

<main class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-9">

            <form id="propose-form" novalidate>

                <!-- SECTION 1: Basic Information — maps to top-level front-matter fields; JS reads them by id= -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h5 mb-4">Basic Information</h2>

                        <!-- TITLE→ front-matter `title:`, required, validated in JS -->
                        <div class="mb-3">
                            <label for="uc-title" class="form-label fw-semibold">Title <span class="text-danger">*</span></label>
                            <input type="text" class="form-control" id="uc-title" placeholder="e.g. Fraud Detection Agent" required>
                            <div class="form-text">A short, descriptive name for the use case.</div>
                        </div>

                        <!-- CATEGORY → front-matter `category:`; options built by Liquid from site.usecase_categories (_config.yml); raw value stored with underscores -->
                        <div class="mb-3">
                            <label for="uc-category" class="form-label fw-semibold">Category <span class="text-danger">*</span></label>
                            <select class="form-select" id="uc-category" required>
                                <option value="">— Select a category —</option>
                                {% for category in site.usecase_categories %}
                                <option value="{{ category }}">{{ category | replace: '_', ' ' }}</option>
                                {% endfor %}
                            </select>
                        </div>

                        <!-- DESCRIPTION → front-matter `description:`, required; shown as card subtitle on the catalogue page -->
                        <div class="mb-3">
                            <label for="uc-description" class="form-label fw-semibold">Short Description <span class="text-danger">*</span></label>
                            <textarea class="form-control" id="uc-description" rows="2" placeholder="One or two sentences describing what the agent does." required></textarea>
                        </div>

                        <!-- END USERS → front-matter `end_user:`, optional, comma-separated roles -->
                        <div class="mb-3">
                            <label for="uc-end-users" class="form-label fw-semibold">End Users</label>
                            <input type="text" class="form-control" id="uc-end-users" placeholder="e.g. Compliance officer, risk analyst">
                        </div>

                        <!-- BUSINESS VALUE → front-matter `business_value:`, optional -->
                        <div class="mb-0">
                            <label for="uc-business-value" class="form-label fw-semibold">Business Value</label>
                            <input type="text" class="form-control" id="uc-business-value" placeholder="e.g. Reduces manual review time by 60%">
                        </div>
                    </div>
                </div>

                <!-- SECTION 2: Related Risks — checkboxes built by Liquid from site.risks; checked values become `related_risks:` YAML list (ri-N format) -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h5 mb-1">Related AI Risks</h2>
                        <p class="text-muted small mb-3">Select all risks that apply to this use case.</p>
                        <div class="row row-cols-1 row-cols-md-2" id="risks-checkboxes">
                            {% assign sorted_risks = site.risks | sort: "sequence" %}
                            {% for risk in sorted_risks %}
                            <div class="col mb-2">
                                <div class="form-check">
                                    <input class="form-check-input risk-check" type="checkbox"
                                           value="ri-{{ risk.sequence }}"
                                           id="risk-{{ risk.sequence }}">
                                    <label class="form-check-label small" for="risk-{{ risk.sequence }}">
                                        <span class="badge bg-secondary me-1" style="font-size:0.65rem;">ri-{{ risk.sequence }}</span>
                                        {{ risk.title }}
                                    </label>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                </div>

                <!-- SECTION 3: Related Mitigations — checkboxes built by Liquid from site.mitigations; checked values become `related_mitigations:` YAML list (mi-N format) -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h5 mb-1">Related Mitigations</h2>
                        <p class="text-muted small mb-3">Select mitigations already in the framework that this use case should reference.</p>
                        <div class="row row-cols-1 row-cols-md-2" id="mitigations-checkboxes">
                            {% assign sorted_mitigations = site.mitigations | sort: "sequence" %}
                            {% for mitigation in sorted_mitigations %}
                            <div class="col mb-2">
                                <div class="form-check">
                                    <input class="form-check-input mitigation-check" type="checkbox"
                                           value="mi-{{ mitigation.sequence }}"
                                           id="mitigation-{{ mitigation.sequence }}">
                                    <label class="form-check-label small" for="mitigation-{{ mitigation.sequence }}">
                                        <span class="badge bg-info text-dark me-1" style="font-size:0.65rem;">mi-{{ mitigation.sequence }}</span>
                                        {{ mitigation.title }}
                                    </label>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                </div>

                <!-- SECTION 4: Data Classifications — checkboxes built by Liquid from _data/data_classification.yml; badges reflect sensitivity level; values become `data_classifications:` YAML list -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h5 mb-1">Data Classifications</h2>
                        <p class="text-muted small mb-3">Which data types does this use case process?</p>
                        <div class="row row-cols-1 row-cols-md-2">
                            {% for dc in site.data.data_classification.financial_data_classification %}
                            <div class="col mb-2">
                                <div class="form-check">
                                    <input class="form-check-input dc-check" type="checkbox"
                                           value="{{ dc.name }}"
                                           id="dc-{{ dc.name }}">
                                    <label class="form-check-label small" for="dc-{{ dc.name }}">
                                        {% if dc.sensitivity == "Critical" %}<span class="badge bg-danger me-1" style="font-size:0.65rem;">Critical</span>
                                        {% elsif dc.sensitivity == "High" %}<span class="badge bg-warning text-dark me-1" style="font-size:0.65rem;">High</span>
                                        {% elsif dc.sensitivity == "Medium" %}<span class="badge bg-info text-dark me-1" style="font-size:0.65rem;">Medium</span>
                                        {% else %}<span class="badge bg-success me-1" style="font-size:0.65rem;">Low</span>{% endif %}
                                        {{ dc.name | replace: '_', ' ' }}
                                    </label>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                </div>

                <!-- SECTION 5: Use Case Description — free-form markdown body; becomes the page content below the front-matter in the generated .md file -->
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h5 mb-1">Use Case Description</h2>
                        <p class="text-muted small mb-3">Describe the use case in detail — architecture, key functions, business value, risks, and any other relevant context. Markdown is supported.</p>
                        <textarea class="form-control font-monospace" id="uc-body" rows="12"
                            placeholder="## Description&#10;&#10;Describe the agent and how it works...&#10;&#10;## Business Value&#10;&#10;Key benefits...&#10;&#10;## AI Risks and Mitigations&#10;&#10;..."></textarea>
                    </div>
                </div>

                <!-- SECTION 6: Submit bar — validates required fields, then opens the pre-filled GitHub Issue URL in a new tab -->
                <div class="d-flex justify-content-between align-items-center">
                    <p class="text-muted small mb-0">Clicking Submit will open a pre-filled GitHub Issue in a new tab. No data is sent to any server.</p>
                    <button type="submit" class="btn btn-primary px-4">Submit Proposal</button>
                </div>

            </form>

        </div>
    </div>
</main>

<script>
// JS: Intercept form submit — collect all field values, build YAML + issue body, open GitHub Issue URL
document.getElementById('propose-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // JS: Read basic text fields by their id= attributes
    var title = document.getElementById('uc-title').value.trim();
    var category = document.getElementById('uc-category').value;
    var description = document.getElementById('uc-description').value.trim();
    var endUsers = document.getElementById('uc-end-users').value.trim();
    var businessValue = document.getElementById('uc-business-value').value.trim();
    var body = document.getElementById('uc-body').value.trim();

    // JS: Guard — required fields must be present before building the URL
    if (!title || !category || !description) {
        alert('Please fill in Title, Category, and Short Description before submitting.');
        return;
    }

    // JS: Collect checked risks — class `.risk-check` applied to every risk checkbox
    var risks = [];
    document.querySelectorAll('.risk-check:checked').forEach(function(cb) {
        risks.push(cb.value);
    });

    // JS: Collect checked mitigations — class `.mitigation-check` applied to every mitigation checkbox
    var mitigations = [];
    document.querySelectorAll('.mitigation-check:checked').forEach(function(cb) {
        mitigations.push(cb.value);
    });

    // JS: Collect checked data classifications — class `.dc-check` applied to every classification checkbox
    var dcs = [];
    document.querySelectorAll('.dc-check:checked').forEach(function(cb) {
        dcs.push(cb.value);
    });

    // JS: Build YAML front-matter string — mirrors the structure of existing use-case .md files
    var yaml = '---\n';
    yaml += 'title: "' + title.replace(/"/g, '\\"') + '"\n';
    yaml += 'layout: usecase\n';
    yaml += 'doc-status: Pre-Draft\n';
    yaml += 'category: ' + category + '\n';
    yaml += '\n';
    yaml += 'description: "' + description.replace(/"/g, '\\"') + '"\n';
    if (endUsers) yaml += 'end_user: "' + endUsers.replace(/"/g, '\\"') + '"\n';
    if (businessValue) yaml += 'business_value: "' + businessValue.replace(/"/g, '\\"') + '"\n';
    yaml += '\n';

    if (risks.length > 0) {
        yaml += 'related_risks:\n';
        risks.forEach(function(r) { yaml += '  - ' + r + '\n'; });
        yaml += '\n';
    }

    if (mitigations.length > 0) {
        yaml += 'related_mitigations:\n';
        mitigations.forEach(function(m) { yaml += '  - ' + m + '\n'; });
        yaml += '\n';
    }

    if (dcs.length > 0) {
        yaml += 'data_classifications:\n';
        dcs.forEach(function(dc) { yaml += '  - name: ' + dc + '\n'; });
    }

    yaml += '---';

    // JS: Build GitHub Issue markdown body — wraps the YAML in a code block so maintainers can copy it directly
    var issueBody = '## Use Case Proposal\n\n';
    issueBody += '_This issue was generated via the [AIGF Proposal Form](https://air-governance-framework.finos.org/propose/use-case/)._\n\n';
    issueBody += '---\n\n';
    issueBody += '### Proposed Front Matter\n\n';
    issueBody += '```yaml\n' + yaml + '\n```\n\n';

    if (body) {
        issueBody += '### Use Case Description\n\n';
        issueBody += body + '\n';
    }

    // JS: Encode title + body and open the GitHub new-issue URL in a new tab; no data is sent to any server
    var issueTitle = '[Use Case Proposal] ' + title;
    var url = 'https://github.com/finos/ai-governance-framework/issues/new'
        + '?title=' + encodeURIComponent(issueTitle)
        + '&body=' + encodeURIComponent(issueBody)
        + '&labels=' + encodeURIComponent('use-case-proposal');

    window.open(url, '_blank');
});
</script>
