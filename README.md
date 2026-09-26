<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/marks/enso-lockup-dark.svg">
  <img src="assets/marks/enso-lockup-light.svg" height="72" alt="Igor Furlan">
</picture>

<p><strong>Site Reliability · Kubernetes · Linux</strong><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marks/tagline-dark.svg"><img src="assets/marks/tagline-light.svg" height="20" alt="living in the terminal, troubleshooting for fun"></picture></p>

Based in Spain. I've spent around 12 years in IT, the last 8 keeping mission-critical
systems running.

Outside work I run two labs on my own hardware and write up what the measurements show,
including the results that proved me wrong.

**[Kubernetes homelab](https://igfurlan.github.io/k8s-portfolio/cluster/architecture/)**:
a bare-metal kubeadm cluster run like production. It has GitOps with ArgoCD, canary releases
gated on Prometheus, full-stack observability, sealed secrets and four layers of off-site
backups.

**[AI inference lab](https://github.com/igfurlan/k3s-llmd-lab)**: three k3s nodes running
llm-d. On identical traffic, prefix-aware routing beat round-robin on cache hit ratio
(84.8% vs 78.4%) at a 14% latency cost.

**Selected write-ups**
- [A benchmark that found nothing](https://igfurlan.github.io/k8s-portfolio/ai-lab/experiment/): why cache-aware routing first tied with round-robin, and the three conditions the test was missing.
- [A feature that was on and doing nothing](https://igfurlan.github.io/k8s-portfolio/ai-lab/routing/): prefill/decode disaggregation reported as enabled for a day without splitting a single request.
- [Canary deployments that roll themselves back](https://igfurlan.github.io/k8s-portfolio/gitops/overview/): Argo Rollouts promoting or aborting a release based on live Prometheus queries.

---

**Certifications**: Kubestronaut · CKA · CKS · KCSA · Red Hat OpenShift: Advanced Application Management · GitLab Certified Associate · *previously held: Microsoft DevOps Engineer Expert · Azure Administrator Associate · HashiCorp Terraform Associate · Oracle Cloud Infrastructure Architect Associate*

**Works with**: Kubernetes · OpenShift · Cilium · Gateway API · ArgoCD · Argo Rollouts · Helm · Kustomize · Prometheus · Grafana · Loki · Velero · Sealed Secrets · llm-d · vLLM · Linux (RHEL family)

**Speaks**: Portuguese · English · Spanish

[Portfolio](https://igfurlan.github.io/k8s-portfolio/) · [LinkedIn](https://www.linkedin.com/in/igorfurlan/)
