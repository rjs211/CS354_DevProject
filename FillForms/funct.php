<?php function domTextReplace( $search, $replace, DOMNode &$domNode, $isRegEx = false ) {
  if ( $domNode->hasChildNodes() ) {
    $children = array();
    // since looping through a DOM being modified is a bad idea we prepare an array:
    foreach ( $domNode->childNodes as $child ) {
      $children[] = $child;
    }
    foreach ( $children as $child ) {
      if ( $child->nodeType === XML_TEXT_NODE ) {
        $oldText = $child->wholeText;
        if ( $isRegEx ) {
          $newText = preg_replace( $search, $replace, $oldText );
        } else {
          $newText = str_replace( $search, $replace, $oldText );
        }
        $newTextNode = $domNode->ownerDocument->createTextNode( $newText );
        $domNode->replaceChild( $newTextNode, $child );
      } else {
        domTextReplace( $search, $replace, $child, $isRegEx );
      }
    }
  }
} ?>
