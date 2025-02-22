---
id: data_docs
title: Data Docs
---
import UniversalMap from '/docs/images/universal_map/_universal_map.mdx';
import TechnicalTag from '../term_tags/_tag.mdx';
import SetupHeader from '/docs/images/universal_map/_um_setup_header.mdx'
import CreateHeader from '/docs/images/universal_map/_um_create_header.mdx';
import ValidateHeader from '/docs/images/universal_map/_um_validate_header.mdx';

<UniversalMap setup='active' connect='inactive' create='active' validate='active'/> 

## Overview

### Definition

Data Docs are human readable documentation generated from Great Expectations metadata detailing <TechnicalTag relative="../" tag="expectation" text="Expectations" />, <TechnicalTag relative="../" tag="validation_result" text="Validation Results" />, etc.

### Features and promises

Data Docs translate Expectations, Validation Results, and other metadata into clean, human-readable documentation. Automatically compiling your data documentation from your data tests in the form of Data Docs guarantees that your documentation will never go stale.

### Relationship to other objects

Data Docs can be used to view <TechnicalTag relative="../" tag="expectation_suite" text="Expectation Suites" /> and Validation Results.  With a customized <TechnicalTag relative="../" tag="renderer" text="Renderer" />, you can extend what they display and how.  You can issue a command to update your Data Docs from your <TechnicalTag relative="../" tag="data_context" text="Data Context" />.  Alternatively, you can include the `UpdateDataDocsAction` <TechnicalTag relative="../" tag="action" text="Action" /> in a <TechnicalTag relative="../" tag="checkpoint" text="Checkpoint's" /> `action_list` to trigger an update of your Data Docs with the Validation Results that were generated by that Checkpoint being run. 

## Use cases

<SetupHeader/>

You can configure multiple Data Docs sites while setting up your Great Expectations project.  This allows you to tailor the information that is displayed by Data Docs as well as how they are hosted.  For more information on setting up your Data Docs, please reference our [guides on how to configure them for specific hosting environments](../guides/setup/index.md#data-docs).

<CreateHeader/>

You can view your saved Expectation Suites in Data Docs.  

<ValidateHeader/>

Saved Validation Results will be displayed in any Data Docs site that is configured to show them.  If you build your Data Docs from the Data Context, the process will render Data Docs for all of your Validation Results.  Alternatively, you can use the `UpdateDataDocsAction` Action in a Checkpoint's `action_list` to update your Data Docs with just the Validation Results generated by that checkpoint.

## Features

### Readability

Data Docs provide a clean, human-readable way to view your Expectation Suites and Validation Results without you having to manually parse their stored values and configurations.  You can also [add comments to your Expectations that will be displayed in your Data Docs](../guides/expectations/advanced/how_to_add_comments_to_expectations_and_display_them_in_data_docs.md), if you feel they need further explanation.

### Versatility

There are multiple use cases for displaying information in your Data Docs.  Three common ones are:

1. Visualize all Great Expectations artifacts from the local repository of a project as HTML: Expectation Suites,
   Validation Results and profiling results.
1. Maintain a "shared source of truth" for a team working on a data project. Such documentation renders all the
   artifacts committed in the source control system (Expectation Suites and profiling results) and a continuously
   updating data quality report, built from a chronological list of validations by run id.
1. Share a spec of a dataset with a client or a partner. This is similar to API documentation in software development.
   This documentation would include profiling results of the dataset to give the reader a quick way to grasp what the
   data looks like, and one or more Expectation Suites that encode what is expected from the data to be considered
   valid.

To support these (and possibly other) use cases Great Expectations has a concept of a "data documentation site". Multiple sites can be configured inside a project, each suitable for a particular data documentation use case.

## API basics

### How to access

Data Docs are rendered as HTML files.  As such, you can open them with any browser.

### How to create

If your Data Docs have not yet been rendered, you can create them from your Data Context.

From the root folder of your project (where you initialized your Data Context), you can build your Data Docs with the CLI command:

```bash title="Terminal command"
great_expectations docs build
```

Alternatively, you can use your Data Context to build your Data Docs in python with the command:
```python title="Python code"
import great_expectations as gx
context = gx.get_context()
context.build_data_docs()
```

### Configuration

Data Docs sites are configured under the `data_docs_sites` key in your deployment's `great_expectations.yml` file. Users can specify:

- which <TechnicalTag relative="../" tag="datasource" text="Datasources" /> to document (by default, all)
- whether to include Expectations, validations and profiling results sections
- where the Expectations and validations should be read from (filesystem, S3, Azure, or GCS)
- where the HTML files should be written (filesystem, S3, Azure, or GCS)
- which <TechnicalTag relative="../" tag="renderer" text="Renderer" /> and view class should be used to render each section

For more information, please see our guides for [how to host and share Data Docs in specific environments](../guides/setup/index.md#data-docs).