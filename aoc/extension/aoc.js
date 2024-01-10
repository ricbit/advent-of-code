const preElements = document.querySelectorAll('pre');

// Iterate over the NodeList
preElements.forEach((elem, index) => {
    // Prepend each <pre> block with an increasing number
    // The 'index + 1' ensures the numbering starts at 1
    elem.innerHTML = `SAMPLE[${index + 1}]<BR>${elem.textContent}`;
});
