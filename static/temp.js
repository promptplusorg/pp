var parseBackgroundColor = function (context, element, backgroundColorOverride) {
    // The function takes three parameters: context, element, and backgroundColorOverride.
    // Context might refer to some kind of context for parsing, and element is the HTML element whose background color needs to be determined.
    // backgroundColorOverride is an optional parameter that can be used to specify a custom background color.

    var ownerDocument = element.ownerDocument;
    // The 'ownerDocument' refers to the document object that owns the current HTML element.

    var documentBackgroundColor = ownerDocument.documentElement
        ? parseColor(context, getComputedStyle(ownerDocument.documentElement).backgroundColor)
        : COLORS.TRANSPARENT;
    // This line checks if the owner document has a root 'html' element.
    // If it does, it gets the computed background color of the 'html' element using getComputedStyle.
    // parseColor is then called to convert this background color into a usable format.
    // If the owner document doesn't have an 'html' element, the background color is set to transparent.

    var bodyBackgroundColor = ownerDocument.body
        ? parseColor(context, getComputedStyle(ownerDocument.body).backgroundColor)
        : COLORS.TRANSPARENT;
    // Similar to the previous line, this checks if the owner document has a 'body' element.
    // If it does, it gets the computed background color of the 'body' element using getComputedStyle.
    // parseColor is used to convert the color, or transparent is used if there's no 'body' element.

    var defaultBackgroundColor = typeof backgroundColorOverride === 'string'
        ? parseColor(context, backgroundColorOverride)
        : backgroundColorOverride === null
            ? COLORS.TRANSPARENT
            : 0xffffffff;
    // This block determines the default background color based on the 'backgroundColorOverride'.
    // If 'backgroundColorOverride' is a string, it's parsed using parseColor.
    // If 'backgroundColorOverride' is null, the background color is set to transparent.
    // Otherwise, if 'backgroundColorOverride' is not null and not a string, it's set to white.

    return element === ownerDocument.documentElement
        ? isTransparent(documentBackgroundColor)
            ? isTransparent(bodyBackgroundColor)
                ? defaultBackgroundColor
                : bodyBackgroundColor
            : documentBackgroundColor
        : defaultBackgroundColor;
    // This block is the main logic of the function.
    // If the element is the 'html' element itself, the function checks if the document background is transparent.
    // If it is, it checks if the body background is also transparent. If both are transparent, it returns the default background color.
    // If the document background is not transparent, it returns the document background color.
    // If the element is not the 'html' element, it returns the default background color.
};
