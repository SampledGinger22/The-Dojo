import React, { useState } from 'react';
import StyledBox from './Style';
import Flex from './Flex';

const DisplayBox = (props) => {
    return (
        <Flex>
            <StyledBox background={ props.boxColor }/>
        </Flex>
    );
}

export default DisplayBox;