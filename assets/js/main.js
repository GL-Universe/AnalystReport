/**
 * AnalystReport - 主页面交互脚本
 * 动态加载报告列表并渲染卡片
 */

document.addEventListener('DOMContentLoaded', async () => {
    await loadReports();
});

async function loadReports() {
    const grid = document.getElementById('reportsGrid');
    const countEl = document.getElementById('reportCount');

    try {
        const response = await fetch('data/reports.json');
        if (!response.ok) throw new Error('无法加载报告列表');
        const data = await response.json();
        const reports = data.reports || [];

        // 更新计数
        countEl.textContent = `${reports.length} 份报告`;

        if (reports.length === 0) {
            grid.innerHTML = `
                <div class="empty-state" style="grid-column: 1 / -1;">
                    <div class="empty-icon">📭</div>
                    <h3>暂无报告</h3>
                    <p>分析报告将在创建后自动显示在这里。</p>
                </div>`;
            return;
        }

        // 按日期降序排列
        reports.sort((a, b) => new Date(b.date) - new Date(a.date));

        // 渲染卡片
        grid.innerHTML = reports.map(r => `
            <a href="${r.file}" class="report-card">
                <div class="card-icon">${r.icon || '📄'}</div>
                <div class="card-title">${escapeHtml(r.title)}</div>
                <div class="card-desc">${escapeHtml(r.description)}</div>
                <div class="card-meta">
                    <span>📅 ${formatDate(r.date)}</span>
                    ${r.author ? `<span>✍️ ${escapeHtml(r.author)}</span>` : ''}
                </div>
                ${r.tags && r.tags.length > 0 ? `
                <div class="tags">
                    ${r.tags.map(t => `<span class="tag tag-${t}">${t}</span>`).join('')}
                </div>` : ''}
            </a>
        `).join('');

    } catch (err) {
        console.error('加载报告失败:', err);
        grid.innerHTML = `
            <div class="empty-state" style="grid-column: 1 / -1;">
                <div class="empty-icon">⚠️</div>
                <h3>加载失败</h3>
                <p>请检查 data/reports.json 文件是否存在且格式正确。</p>
            </div>`;
    }
}

function formatDate(dateStr) {
    const date = new Date(dateStr);
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');
    return `${y}-${m}-${d}`;
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}