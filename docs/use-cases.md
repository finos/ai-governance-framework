---
layout: default
title: "AI Use Cases Catalogue"
permalink: /use-cases/
---

<header class="py-5 bg-light border-bottom">
    <div class="container">
        <div class="text-center">
            <h1 class="display-4">AI Use Cases Catalogue</h1>
            <p class="lead">Explore financial services AI use cases organized by business function and risk profile</p>
        </div>
    </div>
</header>

<main class="container py-5">
    <!-- Search and Filter Section -->
    <div class="row mb-4">
        <div class="col-md-8">
            <input type="text" class="form-control" id="usecase-search" placeholder="Search use cases by title or description...">
        </div>
        <div class="col-md-4">
            <select class="form-select" id="category-filter">
                <option value="all">All Categories</option>
                {% for category in site.usecase_order %}
                <option value="{{ category }}">{{ category | replace: '_', ' ' }}</option>
                {% endfor %}
            </select>
        </div>
    </div>

    <!-- Use Cases Grid by Category -->
    <div id="usecase-grid">
        {% for category in site.usecase_order %}
        {% assign category_usecases = site.usecases | where: "category", category | sort: "sequence" %}
        {% if category_usecases.size > 0 %}
        <div class="category-section mb-5" data-category="{{ category }}">
            <h2 class="mb-4 pb-2 border-bottom">{{ category | replace: '_', ' ' }}</h2>

            <div class="row">
                {% for usecase in category_usecases %}
                <div class="col-md-6 mb-4 usecase-card"
                     data-title="{{ usecase.title | downcase }}"
                     data-description="{{ usecase.description | downcase }}"
                     data-category="{{ category }}">
                    <div class="card h-100 shadow-sm">
                        <div class="card-body">
                            <div class="d-flex align-items-start mb-3">
                                <span class="badge bg-primary me-2" style="font-size: 0.9rem;">
                                    {% include usecase-id.html usecase=usecase %}
                                </span>
                                <h5 class="card-title mb-0">
                                    <a href="{{ usecase.url }}" class="text-decoration-none">{{ usecase.title }}</a>
                                </h5>
                            </div>

                            <p class="card-text text-muted small mb-3">{{ usecase.description }}</p>

                            <!-- Badges -->
                            <div class="d-flex flex-wrap gap-2">
                                {% if usecase.data_classification %}
                                <span class="badge bg-warning text-dark">{{ usecase.data_classification }}</span>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
        {% endfor %}

        <!-- No results message -->
        <div id="no-results" class="text-center text-muted py-5" style="display: none;">
            <p>No use cases found matching your search criteria.</p>
        </div>
    </div>
</main>

<script>
  // Search functionality
  document.getElementById('usecase-search').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const categoryFilter = document.getElementById('category-filter').value;
    filterUseCases(searchTerm, categoryFilter);
  });

  // Category filter
  document.getElementById('category-filter').addEventListener('change', function(e) {
    const selectedCategory = e.target.value;
    const searchTerm = document.getElementById('usecase-search').value.toLowerCase();
    filterUseCases(searchTerm, selectedCategory);
  });

  function filterUseCases(searchTerm, category) {
    const cards = document.querySelectorAll('.usecase-card');
    const sections = document.querySelectorAll('.category-section');
    let visibleCount = 0;

    // Filter cards
    cards.forEach(card => {
      const title = card.getAttribute('data-title');
      const description = card.getAttribute('data-description');
      const cardCategory = card.getAttribute('data-category');

      const matchesSearch = !searchTerm || title.includes(searchTerm) || description.includes(searchTerm);
      const matchesCategory = category === 'all' || cardCategory === category;

      if (matchesSearch && matchesCategory) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    // Hide/show category sections based on visible cards
    sections.forEach(section => {
      const sectionCategory = section.getAttribute('data-category');
      const visibleCardsInSection = section.querySelectorAll('.usecase-card[style="display: block;"], .usecase-card:not([style*="display"])').length;

      if (category === 'all' || sectionCategory === category) {
        if (visibleCardsInSection > 0) {
          section.style.display = 'block';
        } else {
          section.style.display = 'none';
        }
      } else {
        section.style.display = 'none';
      }
    });

    // Show/hide no results message
    const noResults = document.getElementById('no-results');
    if (visibleCount === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }
</script>
