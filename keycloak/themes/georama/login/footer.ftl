<#macro content>
<#-- This will appear on the bottom of the login form from keycloak -->
    <#assign hint = msg("georamaLoginHint")>
    <#if hint?has_content>
        <div id="georama-login-hint" class="georama-login-hint">${kcSanitize(hint)?no_esc}</div>
    </#if>
</#macro>
