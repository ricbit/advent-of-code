const preElements = document.querySelectorAll('pre');
const codeElements = document.querySelectorAll('code:not(pre code)');

// Convert NodeLists to Arrays and merge them
const allElements = Array.from(preElements).concat(Array.from(codeElements));

// Sort allElements based on their position in the document
allElements.sort((a, b) => {
    if (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) {
        return -1;
    } else {
        return 1;
    }
});

// Iterate over the merged and sorted array
allElements.forEach((elem, index) => {
    if (elem.tagName.toLowerCase() === 'pre') {
        // For <pre> elements
        elem.innerHTML = `SAMPLE[${index + 1}]<BR>${elem.innerHTML}`;
    } else if (elem.tagName.toLowerCase() === 'code') {
        // For <code> elements
        const indexTextNode = document.createTextNode(` [[${index + 1}]]`);
        elem.parentNode.insertBefore(indexTextNode, elem.nextSibling);
    }
});

