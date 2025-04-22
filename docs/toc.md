---
layout: default
title: "AI Readiness Governance Framework - Table of Contents"
---

## Risks

{% assign grouped_risks = site.risks | group_by: "type" %}

{% for group in grouped_risks %}
  <h3>{{ group.name }}</h3>
  {% assign sorted_risks = group.items | sort: "sequence" %}
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Type</th>
        <th>Status</th>
        <th>Title</th>
      </tr>
    </thead>
    <tbody>
    {% for risk in sorted_risks %}
      <tr>
        <td><a href="#TR-{{ risk.sequence }}">TR-{{ risk.sequence }}</a></td>
        <td>{{ risk.type }}</td>
        <td>{{ risk["doc-status"] }}</td>
        <td>{{ risk.title }}</td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
{% endfor %}



### Mitigations
{% assign sorted_mitigations = site.mitigations | sort: 'sequence' %}
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Status</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
  {% for mitigation in sorted_mitigations %}
    <tr>
      <td><a href="#CT-{{ mitigation.sequence }}">CT-{{ mitigation.sequence }}</a></td>
      <td>{{ mitigation.doc-status }}</td>
      <td>{{ mitigation.title }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>