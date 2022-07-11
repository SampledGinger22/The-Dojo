import React from 'react';
import styled from 'styled-components';

const StyledBox = styled.div`
    width: 100px;
    height: 100px;
    background: ${props => props.boxColor};
    margin-left: 20px;
;`

export default StyledBox;

