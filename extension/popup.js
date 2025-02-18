document.getElementById('convert-button').addEventListener('click', async () => {
    const latexCode = document.getElementById('latex-input').value;
  
    const apiUrl = process.env.SERVER_URL; // Consider moving this to an environment variable for better security and configurability
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ latex: latexCode })
    });
  
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'document.docx';
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
  });
  