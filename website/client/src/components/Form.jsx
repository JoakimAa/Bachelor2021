import React from 'react';
import styled from 'styled-components';
import PropTypes from 'prop-types';

const Form = ({ formState, error, handleSubmit, onSubmit, register }) => (
  <StyledForm onSubmit={handleSubmit(onSubmit)}>
    <FormGroup>
      <InputLabel htmlFor="type">Type</InputLabel>
      <Input
        type="text"
        name="type"
        id="type"
        placeholder="Type"
        ref={register({
          required: true,
        })}
      />
    </FormGroup>
    <FormGroup>
      <InputLabel htmlFor="amount">Pris</InputLabel>
      <Input
        type="text"
        name="amount"
        id="amount"
        placeholder="Pris"
        ref={register({
          required: true,
        })}
      />
    </FormGroup>
    <FormGroup>
      <InputLabel htmlFor="date">Dato</InputLabel>
      <Input
        type="date"
        name="date"
        id="date"
        placeholder="Date"
        ref={register({
          required: true,
        })}
      />
    </FormGroup>
    <FormGroup>
      <StyledButton type="submit" isLoading={formState.isSubmitting}>
        Send inn
      </StyledButton>
      {error && <p>{error.message}</p>}
    </FormGroup>
  </StyledForm>
);

export default Form;

Form.propTypes = {
  formState: PropTypes.object,
  error: PropTypes.object,
  handleSubmit: PropTypes.func,
  onSubmit: PropTypes.func,
  register: PropTypes.func,
};

const Input = styled.input`
  border-bottom: solid 0.1rem black;
  margin: 0.2rem 0rem;
`;

const FormGroup = styled.div`
  margin: 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
`;

const StyledForm = styled.form`
  margin: 1.5rem;
`;

const StyledButton = styled.button`
  padding: 0.2rem 0.6rem;
  border: solid 0.1rem black;
`;

const InputLabel = styled.label``;
