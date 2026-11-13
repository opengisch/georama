<!-- {{ env "REPORT" }} -->
### Trivy: {{ env "REPORT" }}, HIGH and CRITICAL ({{ env "HEAD_SHA" }})
{{- $clean := true }}
{{- range . }}
{{- if .Vulnerabilities }}
{{- $clean = false }}

**{{ .Target }}**

| Severity | Package | Vulnerability | Installed | Fixed |
| --- | --- | --- | --- | --- |
{{- range .Vulnerabilities }}
| {{ .Severity }} | `{{ .PkgName }}` | {{ if .PrimaryURL }}[{{ .VulnerabilityID }}]({{ .PrimaryURL }}){{ else }}{{ .VulnerabilityID }}{{ end }} | {{ .InstalledVersion }} | {{ .FixedVersion }} |
{{- end }}
{{- end }}
{{- end }}
{{- if $clean }}

No findings.
{{- end }}
