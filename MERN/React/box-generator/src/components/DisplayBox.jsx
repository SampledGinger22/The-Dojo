import React, { useState } from 'react';
import StyledBox from './Style';
import Flex from './Flex';

const displayBox = (props) => {
    return (
        <Flex>
            <StyledBox bgColor={ props.boxColor }/>
        </Flex>
    );
}

export default displayBox;