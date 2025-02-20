from __future__ import annotations

import logging
import pathlib
import re
from typing import TYPE_CHECKING, Optional, Union

from typing_extensions import Literal

from great_expectations.experimental.datasources import _PandasFilePathDatasource
from great_expectations.experimental.datasources.data_asset.data_connector import (
    DataConnector,
    FilesystemDataConnector,
)
from great_expectations.experimental.datasources.interfaces import (
    BatchSortersDefinition,
    TestConnectionError,
)
from great_expectations.experimental.datasources.pandas_file_path_datasource import (
    CSVAsset,
    ExcelAsset,
    JSONAsset,
    ParquetAsset,
)
from great_expectations.experimental.datasources.signatures import _merge_signatures

if TYPE_CHECKING:
    from great_expectations.experimental.datasources.interfaces import BatchSorter

logger = logging.getLogger(__name__)


class PandasFilesystemDatasource(_PandasFilePathDatasource):
    # instance attributes
    type: Literal["pandas_filesystem"] = "pandas_filesystem"

    # Filesystem specific attributes
    base_directory: pathlib.Path
    data_context_root_directory: Optional[pathlib.Path] = None

    def test_connection(self, test_assets: bool = True) -> None:
        """Test the connection for the PandasFilesystemDatasource.

        Args:
            test_assets: If assets have been passed to the PandasFilesystemDatasource, whether to test them as well.

        Raises:
            TestConnectionError: If the connection test fails.
        """
        if not self.base_directory.exists():
            raise TestConnectionError(
                f"Path: {self.base_directory.resolve()} does not exist."
            )

        if self.assets and test_assets:
            for asset in self.assets.values():
                asset.test_connection()

    def add_csv_asset(
        self,
        name: str,
        batching_regex: Optional[Union[re.Pattern, str]] = None,
        glob_directive: str = "**/*",
        order_by: Optional[BatchSortersDefinition] = None,
        **kwargs,  # TODO: update signature to have specific keys & types
    ) -> CSVAsset:  # type: ignore[valid-type]
        """Adds a CSV DataAsst to the present "PandasFilesystemDatasource" object.

        Args:
            name: The name of the csv asset
            batching_regex: regex pattern that matches csv filenames that is used to label the batches
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            order_by: sorting directive via either list[BatchSorter] or "{+|-}key" syntax: +/- (a/de)scending; + default
            kwargs: Extra keyword arguments should correspond to ``pandas.read_csv`` keyword args
        """
        batching_regex_pattern: re.Pattern = self.parse_batching_regex_string(
            batching_regex=batching_regex
        )
        order_by_sorters: list[BatchSorter] = self.parse_order_by_sorters(
            order_by=order_by
        )

        asset = CSVAsset(
            name=name,
            batching_regex=batching_regex_pattern,
            order_by=order_by_sorters,
            **kwargs,
        )

        data_connector: DataConnector = FilesystemDataConnector(
            datasource_name=self.name,
            data_asset_name=name,
            batching_regex=batching_regex_pattern,
            base_directory=self.base_directory,
            glob_directive=glob_directive,
            data_context_root_directory=self.data_context_root_directory,
        )
        test_connection_error_message: str = f"""No file at base_directory path "{self.base_directory.resolve()}" matched regular expressions pattern "{batching_regex_pattern.pattern}" and/or glob_directive "{glob_directive}" for DataAsset "{name}"."""
        return self.add_asset(
            asset=asset,
            data_connector=data_connector,
            test_connection_error_message=test_connection_error_message,
        )

    def add_excel_asset(
        self,
        name: str,
        batching_regex: Optional[Union[str, re.Pattern]] = None,
        glob_directive: str = "**/*",
        order_by: Optional[BatchSortersDefinition] = None,
        **kwargs,  # TODO: update signature to have specific keys & types
    ) -> ExcelAsset:  # type: ignore[valid-type]
        """Adds an Excel DataAsst to the present "PandasFilesystemDatasource" object.

        Args:
            name: The name of the csv asset
            batching_regex: regex pattern that matches csv filenames that is used to label the batches
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            order_by: sorting directive via either list[BatchSorter] or "{+|-}key" syntax: +/- (a/de)scending; + default
            kwargs: Extra keyword arguments should correspond to ``pandas.read_excel`` keyword args
        """
        batching_regex_pattern: re.Pattern = self.parse_batching_regex_string(
            batching_regex=batching_regex
        )
        order_by_sorters: list[BatchSorter] = self.parse_order_by_sorters(
            order_by=order_by
        )

        asset = ExcelAsset(
            name=name,
            batching_regex=batching_regex_pattern,
            order_by=order_by_sorters,
            **kwargs,
        )

        data_connector: DataConnector = FilesystemDataConnector(
            datasource_name=self.name,
            data_asset_name=name,
            batching_regex=batching_regex_pattern,
            base_directory=self.base_directory,
            glob_directive=glob_directive,
            data_context_root_directory=self.data_context_root_directory,
        )
        test_connection_error_message: str = f"""No file at base_directory path "{self.base_directory.resolve()}" matched regular expressions pattern "{batching_regex_pattern.pattern}" and/or glob_directive "{glob_directive}" for DataAsset "{name}"."""
        return self.add_asset(
            asset=asset,
            data_connector=data_connector,
            test_connection_error_message=test_connection_error_message,
        )

    def add_json_asset(
        self,
        name: str,
        batching_regex: Optional[Union[str, re.Pattern]] = None,
        glob_directive: str = "**/*",
        order_by: Optional[BatchSortersDefinition] = None,
        **kwargs,  # TODO: update signature to have specific keys & types
    ) -> JSONAsset:  # type: ignore[valid-type]
        """Adds a JSON DataAsst to the present "PandasFilesystemDatasource" object.

        Args:
            name: The name of the csv asset
            batching_regex: regex pattern that matches csv filenames that is used to label the batches
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            order_by: sorting directive via either list[BatchSorter] or "{+|-}key" syntax: +/- (a/de)scending; + default
            kwargs: Extra keyword arguments should correspond to ``pandas.read_json`` keyword args
        """
        batching_regex_pattern: re.Pattern = self.parse_batching_regex_string(
            batching_regex=batching_regex
        )
        order_by_sorters: list[BatchSorter] = self.parse_order_by_sorters(
            order_by=order_by
        )

        asset = JSONAsset(
            name=name,
            batching_regex=batching_regex_pattern,
            order_by=order_by_sorters,
            **kwargs,
        )

        data_connector: DataConnector = FilesystemDataConnector(
            datasource_name=self.name,
            data_asset_name=name,
            batching_regex=batching_regex_pattern,
            base_directory=self.base_directory,
            glob_directive=glob_directive,
            data_context_root_directory=self.data_context_root_directory,
        )
        test_connection_error_message: str = f"""No file at base_directory path "{self.base_directory.resolve()}" matched regular expressions pattern "{batching_regex_pattern.pattern}" and/or glob_directive "{glob_directive}" for DataAsset "{name}"."""
        return self.add_asset(
            asset=asset,
            data_connector=data_connector,
            test_connection_error_message=test_connection_error_message,
        )

    def add_parquet_asset(
        self,
        name: str,
        batching_regex: Optional[Union[str, re.Pattern]] = None,
        glob_directive: str = "**/*",
        order_by: Optional[BatchSortersDefinition] = None,
        **kwargs,  # TODO: update signature to have specific keys & types
    ) -> ParquetAsset:  # type: ignore[valid-type]
        """Adds a Parquet DataAsst to the present "PandasFilesystemDatasource" object.

        Args:
            name: The name of the csv asset
            batching_regex: regex pattern that matches csv filenames that is used to label the batches
            glob_directive: glob for selecting files in directory (defaults to `**/*`) or nested directories (e.g. `*/*/*.csv`)
            order_by: sorting directive via either list[BatchSorter] or "{+|-}key" syntax: +/- (a/de)scending; + default
            kwargs: Extra keyword arguments should correspond to ``pandas.read_parquet`` keyword args
        """
        batching_regex_pattern: re.Pattern = self.parse_batching_regex_string(
            batching_regex=batching_regex
        )
        order_by_sorters: list[BatchSorter] = self.parse_order_by_sorters(
            order_by=order_by
        )

        asset = ParquetAsset(
            name=name,
            batching_regex=batching_regex_pattern,
            order_by=order_by_sorters,
            **kwargs,
        )

        data_connector: DataConnector = FilesystemDataConnector(
            datasource_name=self.name,
            data_asset_name=name,
            batching_regex=batching_regex_pattern,
            base_directory=self.base_directory,
            glob_directive=glob_directive,
            data_context_root_directory=self.data_context_root_directory,
        )
        test_connection_error_message: str = f"""No file at base_directory path "{self.base_directory.resolve()}" matched regular expressions pattern "{batching_regex_pattern.pattern}" and/or glob_directive "{glob_directive}" for DataAsset "{name}"."""
        return self.add_asset(
            asset=asset,
            data_connector=data_connector,
            test_connection_error_message=test_connection_error_message,
        )

    # attr-defined issue
    # https://github.com/python/mypy/issues/12472
    add_csv_asset.__signature__ = _merge_signatures(add_csv_asset, CSVAsset, exclude={"type"})  # type: ignore[attr-defined]
    add_excel_asset.__signature__ = _merge_signatures(add_excel_asset, ExcelAsset, exclude={"type"})  # type: ignore[attr-defined]
    add_json_asset.__signature__ = _merge_signatures(add_json_asset, JSONAsset, exclude={"type"})  # type: ignore[attr-defined]
    add_parquet_asset.__signature__ = _merge_signatures(add_parquet_asset, ParquetAsset, exclude={"type"})  # type: ignore[attr-defined]
