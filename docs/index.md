---
layout: index
title: "FINOS AI Governance Framework"
subtitle: "A comprehensive collection of risks and mitigations that support on-boarding, development of, and running Generative AI solutions"
risk_order:
  - OP
  - SEC
  - RC
mitigation_order:
  - PREV
  - DET
---

AI, especially Generative AI, is reshaping financial services, enhancing products, client interactions, and productivity. However, challenges like hallucinations and model unpredictability make safe deployment complex. Rapid advancements require flexible governance.

Financial institutions are eager to adopt AI but face regulatory hurdles. Existing frameworks may not address AI's unique risks, necessitating an adaptive governance model for safe and compliant integration.

The following framework has been developed by [FINOS (Fintech Open Source Foundation)](https://www.finos.org/) members, providing a comprehensive catalogue of risks and associated mitigations. We suggest using our [heuristic risk identification framework](heuristic-assessment.html) to determine which risks are most relevant for a given use case.

<!-- Search and Filter Controls -->
<div class="row mb-4">
    <div class="col-12">
        <div class="card border-0 bg-light">
            <div class="card-body">
                <div class="row g-3">
                    <div class="col-md-5">
                        <label for="searchInput" class="form-label fw-bold">Search</label>
                        <input type="text" class="form-control" id="searchInput" placeholder="Search risks and mitigations by title or content...">
                    </div>
                    <div class="col-md-2">
                        <label for="typeFilter" class="form-label fw-bold">Filter by Type</label>
                        <select class="form-select" id="typeFilter">
                            <option value="">All Types</option>
                            <option value="risk">Risks Only</option>
                            <option value="mitigation">Mitigations Only</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label fw-bold">Filter by Category</label>
                        <div class="card border">
                            <div class="card-body p-2">
                                <div class="row g-2">
                                    <div class="col-6">
                                        <div class="small text-muted fw-bold mb-2">
                                            <i class="bi bi-asterisk me-1"></i>Risks
                                        </div>
                                        <div class="form-check form-check-sm mb-1">
                                            <input class="form-check-input category-checkbox" type="checkbox" value="OP" id="cat-OP" data-type="risk">
                                            <label class="form-check-label small" for="cat-OP">
                                                <i class="bi bi-person-fill-gear me-1"></i>Operational
                                            </label>
                                        </div>
                                        <div class="form-check form-check-sm mb-1">
                                            <input class="form-check-input category-checkbox" type="checkbox" value="SEC" id="cat-SEC" data-type="risk">
                                            <label class="form-check-label small" for="cat-SEC">
                                                <i class="bi bi-bug-fill me-1"></i>Security
                                            </label>
                                        </div>
                                        <div class="form-check form-check-sm mb-0">
                                            <input class="form-check-input category-checkbox" type="checkbox" value="RC" id="cat-RC" data-type="risk">
                                            <label class="form-check-label small" for="cat-RC">
                                                <i class="bi bi-clipboard2-check-fill me-1"></i>Regulatory
                                            </label>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="small text-muted fw-bold mb-2">
                                            <i class="bi bi-shield-shaded me-1"></i>Mitigations
                                        </div>
                                        <div class="form-check form-check-sm mb-1">
                                            <input class="form-check-input category-checkbox" type="checkbox" value="PREV" id="cat-PREV" data-type="mitigation">
                                            <label class="form-check-label small" for="cat-PREV">
                                                <i class="bi bi-lock-fill me-1"></i>Preventative
                                            </label>
                                        </div>
                                        <div class="form-check form-check-sm mb-0">
                                            <input class="form-check-input category-checkbox" type="checkbox" value="DET" id="cat-DET" data-type="mitigation">
                                            <label class="form-check-label small" for="cat-DET">
                                                <i class="bi bi-eye-fill me-1"></i>Detective
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <label class="form-label fw-bold">&nbsp;</label>
                        <button type="button" class="btn btn-outline-secondary w-100" id="resetFilters">
                            Reset
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Main Catalogue Cards -->
<div class="row mb-5" id="catalogueRow">
    <div class="col-md-6">
        <div class="card h-100 shadow border-0">
            <div class="card-header bg-primary text-white">
                <div class="d-flex justify-content-between align-items-center">
                    <h2 class="h4 mb-0">
                        <i class="bi bi-asterisk me-2"></i>Risk Catalogue
                    </h2>
                    <button class="btn btn-outline-light btn-sm expand-btn" type="button" data-catalogue="risk">
                        <i class="bi bi-chevron-bar-right"></i>
                    </button>
                </div>
            </div>
            <div class="collapse show" id="riskCatalogue">
                <div class="card-body">
                    <p class="text-muted mb-4">Identify potential risks in your AI implementation across operational, security, and regulatory dimensions.</p>
                    
                    {% for order in page.risk_order %}
                      {% assign risk_group = site.risks | group_by: "type" | where: "name", order | first %}
                      {% if risk_group %}
                      <div class="mb-4">
                          <div class="d-flex justify-content-between align-items-center mb-2">
                              <h3 class="h5 mb-0 text-primary">
                                  {% if order == 'OP' %}
                                      <i class="bi bi-person-fill-gear me-2"></i>
                                  {% elsif order == 'SEC' %}
                                      <i class="bi bi-bug-fill me-2"></i>
                                  {% elsif order == 'RC' %}
                                      <i class="bi bi-clipboard2-check-fill me-2"></i>
                                  {% endif %}
                                  {{ site.risk_classification[risk_group.name] }}
                              </h3>
                              <span class="badge bg-primary">{{ risk_group.items | size }} risks</span>
                          </div>
                          <div class="row g-2" data-category="{{ order }}" data-type="risk">
                              {% assign sorted_risks = risk_group.items | sort: "sequence" %}
                              {% for risk in sorted_risks %}
                              <div class="col-12 risk-item" data-title="{{ risk.title | downcase }}" data-content="{{ risk.content | strip_html | strip_newlines | downcase }}">
                                  <div class="card border-start border-primary border-3 h-100">
                                      <div class="card-body py-2">
                                          <div class="d-flex justify-content-between align-items-start">
                                              <div class="flex-grow-1">
                                                  <div class="risk-id small text-muted mb-1">
                                                    {% include risk-id.html risk=risk %}
                                                  </div>
                                                  <h4 class="h6 mb-1">{{ risk.title }}</h4>
                                                  {% assign raw_content = risk.content | strip_html | strip_newlines %}
                                                  {% assign content_after_summary = raw_content | split: "Summary" %}
                                                  {% if content_after_summary.size > 1 %}
                                                    {% assign clean_summary = content_after_summary[1] | strip %}
                                                  {% else %}
                                                    {% assign content_after_desc = raw_content | split: "Description" %}
                                                    {% if content_after_desc.size > 1 %}
                                                      {% assign clean_summary = content_after_desc[1] | strip %}
                                                    {% else %}
                                                      {% assign clean_summary = raw_content | strip %}
                                                    {% endif %}
                                                  {% endif %}
                                                  <p class="small text-muted mb-0 description-text">{{ clean_summary }}</p>
                                              </div>
                                              <div class="d-flex flex-column gap-1 ms-2">
                                                  <a href="{{ risk.id }}.html" class="btn btn-outline-primary btn-sm">
                                                      View
                                                  </a>
                                                  <a href="https://github.com/finos/ai-governance-framework/edit/main/docs/{{ risk.path }}" 
                                                     target="_blank" 
                                                     class="btn btn-outline-primary btn-sm">
                                                      Edit
                                                  </a>
                                              </div>
                                          </div>
                                      </div>
                                  </div>
                              </div>
                              {% endfor %}
                          </div>
                      </div>
                      {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-6">
        <div class="card h-100 shadow border-0">
            <div class="card-header bg-success text-white">
                <div class="d-flex justify-content-between align-items-center">
                    <h2 class="h4 mb-0">
                        <i class="bi bi-shield-shaded me-2"></i>Mitigation Catalogue
                    </h2>
                    <button class="btn btn-outline-light btn-sm expand-btn" type="button" data-catalogue="mitigation">
                        <i class="bi bi-chevron-bar-left"></i>
                    </button>
                </div>
            </div>
            <div class="collapse show" id="mitigationCatalogue">
                <div class="card-body">
                    <p class="text-muted mb-4">Discover preventative and detective controls to mitigate identified risks in your AI systems.</p>
                    
                    {% for order in page.mitigation_order %}
                      {% assign mitigation_group = site.mitigations | group_by: "type" | where: "name", order | first %}
                      {% if mitigation_group %}
                      <div class="mb-4">
                          <div class="d-flex justify-content-between align-items-center mb-2">
                              <h3 class="h5 mb-0 text-success">
                                  {% if order == 'PREV' %}
                                      <i class="bi bi-lock-fill me-2"></i>
                                  {% elsif order == 'DET' %}
                                      <i class="bi bi-eye-fill me-2"></i>
                                  {% endif %}
                                  {{ site.mitigation_classification[mitigation_group.name] }}
                              </h3>
                              <span class="badge bg-success">{{ mitigation_group.items | size }} mitigations</span>
                          </div>
                          <div class="row g-2" data-category="{{ order }}" data-type="mitigation">
                              {% assign sorted_mitigations = mitigation_group.items | sort: "sequence" %}
                              {% for mitigation in sorted_mitigations %}
                              <div class="col-12 mitigation-item" data-title="{{ mitigation.title | downcase }}" data-content="{{ mitigation.content | strip_html | strip_newlines | downcase }}">
                                  <div class="card border-start border-success border-3 h-100">
                                      <div class="card-body py-2">
                                          <div class="d-flex justify-content-between align-items-start">
                                              <div class="flex-grow-1">
                                                  <div class="mitigation-id small text-muted mb-1">
                                                    {% include mitigation-id.html mitigation=mitigation %}
                                                  </div>
                                                  <h4 class="h6 mb-1">{{ mitigation.title }}</h4>
                                                  {% assign raw_content = mitigation.content | strip_html | strip_newlines %}
                                                  {% assign content_after_summary = raw_content | split: "Summary" %}
                                                  {% if content_after_summary.size > 1 %}
                                                    {% assign clean_summary = content_after_summary[1] | strip %}
                                                  {% else %}
                                                    {% assign content_after_purpose = raw_content | split: "Purpose" %}
                                                    {% if content_after_purpose.size > 1 %}
                                                      {% assign clean_summary = content_after_purpose[1] | strip %}
                                                    {% else %}
                                                      {% assign content_after_desc = raw_content | split: "Description" %}
                                                      {% if content_after_desc.size > 1 %}
                                                        {% assign clean_summary = content_after_desc[1] | strip %}
                                                      {% else %}
                                                        {% assign clean_summary = raw_content | strip %}
                                                      {% endif %}
                                                    {% endif %}
                                                  {% endif %}
                                                  <p class="small text-muted mb-0 description-text">{{ clean_summary }}</p>
                                              </div>
                                              <div class="d-flex flex-column gap-1 ms-2">
                                                  <a href="{{ mitigation.id }}.html" class="btn btn-outline-success btn-sm">
                                                      View
                                                  </a>
                                                  <a href="https://github.com/finos/ai-governance-framework/edit/main/docs/{{ mitigation.path }}" 
                                                     target="_blank" 
                                                     class="btn btn-outline-success btn-sm">
                                                      Edit
                                                  </a>
                                              </div>
                                          </div>
                                      </div>
                                  </div>
                              </div>
                              {% endfor %}
                          </div>
                      </div>
                      {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const typeFilter = document.getElementById('typeFilter');
    const resetButton = document.getElementById('resetFilters');
    const riskCatalogue = document.getElementById('riskCatalogue');
    const mitigationCatalogue = document.getElementById('mitigationCatalogue');
    const riskColumn = riskCatalogue.closest('.col-md-6');
    const mitigationColumn = mitigationCatalogue.closest('.col-md-6');
    
    // State management
    let catalogueStates = {
        risk: { expanded: false },
        mitigation: { expanded: false }
    };
    
    // Apply visual states
    function applyCatalogueStates() {
        const selectedType = typeFilter.value;
        
        // Determine visibility based on expand states and type filter
        const riskVisible = !catalogueStates.mitigation.expanded && (selectedType !== 'mitigation');
        const mitigationVisible = !catalogueStates.risk.expanded && (selectedType !== 'risk');
        
        // Handle Risk Catalogue
        if (!riskVisible) {
            riskColumn.style.display = 'none';
        } else {
            riskColumn.style.display = 'block';
            riskColumn.className = catalogueStates.risk.expanded || !mitigationVisible ? 'col-12' : 'col-md-6';
        }
        
        // Handle Mitigation Catalogue
        if (!mitigationVisible) {
            mitigationColumn.style.display = 'none';
        } else {
            mitigationColumn.style.display = 'block';
            mitigationColumn.className = catalogueStates.mitigation.expanded || !riskVisible ? 'col-12' : 'col-md-6';
        }
        
        // Update button states
        updateExpandButton('risk', catalogueStates.risk.expanded);
        updateExpandButton('mitigation', catalogueStates.mitigation.expanded);
    }
    
    // Update expand button appearance
    function updateExpandButton(type, isExpanded) {
        const button = document.querySelector(`[data-catalogue="${type}"]`);
        if (button) {
            if (type === 'risk') {
                if (isExpanded) {
                    // When risk is expanded, show left arrow to collapse it back
                    button.innerHTML = `<i class="bi bi-chevron-bar-left"></i>`;
                } else {
                    // When risk is not expanded, show right arrow to expand it
                    button.innerHTML = `<i class="bi bi-chevron-bar-right"></i>`;
                }
            } else { // mitigation
                if (isExpanded) {
                    // When mitigation is expanded, show right arrow to collapse it back
                    button.innerHTML = `<i class="bi bi-chevron-bar-right"></i>`;
                } else {
                    // When mitigation is not expanded, show left arrow to expand it
                    button.innerHTML = `<i class="bi bi-chevron-bar-left"></i>`;
                }
            }
        }
    }
    
    // Filter items and update catalogue visibility
    function filterItems() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedType = typeFilter.value;
        const categoryCheckboxes = document.querySelectorAll('.category-checkbox');
        const selectedCategories = Array.from(categoryCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);
        
        let riskCount = 0;
        let mitigationCount = 0;
        
        // Filter items
        ['risk', 'mitigation'].forEach(type => {
            document.querySelectorAll(`.${type}-item`).forEach(item => {
                const title = item.getAttribute('data-title') || '';
                const content = item.getAttribute('data-content') || '';
                const parentSection = item.closest('[data-category]');
                const itemCategory = parentSection?.getAttribute('data-category') || '';
                
                const matchesSearch = !searchTerm || title.includes(searchTerm) || content.includes(searchTerm);
                const matchesType = !selectedType || selectedType === type;
                const matchesCategory = selectedCategories.length === 0 || selectedCategories.includes(itemCategory);
                
                const isVisible = matchesSearch && matchesType && matchesCategory;
                item.style.display = isVisible ? 'block' : 'none';
                
                // Count visible items
                if (isVisible) {
                    if (type === 'risk') {
                        riskCount++;
                    } else {
                        mitigationCount++;
                    }
                }
            });
        });
        
        // Update category section visibility and badges
        document.querySelectorAll('[data-category]').forEach(section => {
            const categoryType = section.getAttribute('data-category');
            const sectionType = section.getAttribute('data-type');
            const visibleItems = section.querySelectorAll(`.${sectionType}-item:not([style*="display: none"])`);
            
            const shouldShow = (!selectedType || selectedType === sectionType) && 
                             (selectedCategories.length === 0 || selectedCategories.includes(categoryType)) &&
                             visibleItems.length > 0;
            
            const container = section.closest('.mb-4');
            if (container) container.style.display = shouldShow ? 'block' : 'none';
            
            // Update individual category badges
            const badge = container?.querySelector('.badge');
            if (badge && shouldShow) {
                const count = visibleItems.length;
                const itemType = sectionType === 'risk' ? 'risk' : 'mitigation';
                badge.textContent = `${count} ${itemType}${count !== 1 ? 's' : ''}`;
            }
        });
        
        // Update main catalogue header badges
        const riskHeader = document.querySelector('#riskCatalogue').closest('.card').querySelector('.card-header h2');
        const mitigationHeader = document.querySelector('#mitigationCatalogue').closest('.card').querySelector('.card-header h2');
        
        // Update or create badges in headers
        updateHeaderBadge(riskHeader, riskCount, 'risk');
        updateHeaderBadge(mitigationHeader, mitigationCount, 'mitigation');
        
        applyCatalogueStates();
    }
    
    // Helper function to update header badges
    function updateHeaderBadge(header, count, type) {
        if (!header) return;
        
        // Remove existing badge if any
        const existingBadge = header.querySelector('.count-badge');
        if (existingBadge) {
            existingBadge.remove();
        }
        
        // Create new badge
        const badge = document.createElement('span');
        badge.className = `badge ${type === 'risk' ? 'bg-light text-primary' : 'bg-light text-success'} ms-2 count-badge`;
        badge.textContent = `${count} ${type}${count !== 1 ? 's' : ''}`;
        header.appendChild(badge);
    }
    
    // Update checkbox visibility and enabled state based on type selection
    function updateCategoryOptions() {
        const selectedType = typeFilter.value;
        const riskCheckboxes = document.querySelectorAll('.category-checkbox[data-type="risk"]');
        const mitigationCheckboxes = document.querySelectorAll('.category-checkbox[data-type="mitigation"]');
        const riskColumn = document.querySelector('.col-6:first-child');
        const mitigationColumn = document.querySelector('.col-6:last-child');
        
        // Handle risk checkboxes and column
        if (selectedType === 'mitigation') {
            // Grey out risk checkboxes when only mitigations are selected
            riskCheckboxes.forEach(checkbox => {
                checkbox.disabled = true;
                checkbox.checked = false;
            });
            riskColumn.style.opacity = '0.5';
        } else {
            // Enable risk checkboxes
            riskCheckboxes.forEach(checkbox => {
                checkbox.disabled = false;
            });
            riskColumn.style.opacity = '1';
        }
        
        // Handle mitigation checkboxes and column
        if (selectedType === 'risk') {
            // Grey out mitigation checkboxes when only risks are selected
            mitigationCheckboxes.forEach(checkbox => {
                checkbox.disabled = true;
                checkbox.checked = false;
            });
            mitigationColumn.style.opacity = '0.5';
        } else {
            // Enable mitigation checkboxes
            mitigationCheckboxes.forEach(checkbox => {
                checkbox.disabled = false;
            });
            mitigationColumn.style.opacity = '1';
        }
        
        // Re-attach event listeners to all checkboxes (enabled ones)
        document.querySelectorAll('.category-checkbox:not(:disabled)').forEach(checkbox => {
            // Remove existing listeners to prevent duplicates
            checkbox.removeEventListener('change', filterItems);
            checkbox.addEventListener('change', filterItems);
        });
    }
    
    // Reset all filters and search
    function resetAllFilters() {
        searchInput.value = '';
        typeFilter.value = '';
        
        // Uncheck and enable all category checkboxes
        document.querySelectorAll('.category-checkbox').forEach(checkbox => {
            checkbox.checked = false;
            checkbox.disabled = false;
        });
        
        // Reset column opacity
        document.querySelectorAll('.col-6').forEach(column => {
            column.style.opacity = '1';
        });
        
        // Reset expand states
        catalogueStates.risk.expanded = false;
        catalogueStates.mitigation.expanded = false;
        
        // Update category options and apply states
        updateCategoryOptions();
        filterItems();
    }
    
    // Handle expand button clicks
    document.querySelectorAll('.expand-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const catalogueType = this.getAttribute('data-catalogue');
            
            // Toggle the expanded state
            catalogueStates[catalogueType].expanded = !catalogueStates[catalogueType].expanded;
            
            // If expanding this catalogue, collapse the other one
            if (catalogueStates[catalogueType].expanded) {
                const otherType = catalogueType === 'risk' ? 'mitigation' : 'risk';
                catalogueStates[otherType].expanded = false;
                
                // Update type filter to match the expanded catalogue
                typeFilter.value = catalogueType;
                updateCategoryOptions();
            } else {
                // If collapsing, reset to show all types
                typeFilter.value = '';
                updateCategoryOptions();
            }
            
            filterItems();
        });
    });
    
    // Event listeners
    searchInput.addEventListener('input', filterItems);
    typeFilter.addEventListener('change', function() {
        updateCategoryOptions();
        filterItems();
    });
    resetButton.addEventListener('click', resetAllFilters);
    
    // Initialize
    updateCategoryOptions();
    applyCatalogueStates();
    
    // Add initial event listeners to category checkboxes
    document.querySelectorAll('.category-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', filterItems);
    });
});
</script>

